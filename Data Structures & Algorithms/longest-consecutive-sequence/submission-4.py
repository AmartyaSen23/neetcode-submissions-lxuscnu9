class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash={}
        result={}
        nums.sort()
        for num in nums:
            if num-1 in hash:
                if (num in hash):
                    continue
                result[num]=result[num-1]+1
                hash[num]=1
            else:
                hash[num]=1
                result[num]=1
        return max(result.values())