class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        result=[]
        for num in nums:
            if (num in hash):
                hash[num]=hash[num]+1
                continue
            hash[num]=1
        for i in range(k):
            j=max(hash, key=hash.get)
            result.append(j)
            hash.pop(j)
        return result