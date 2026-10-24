class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i,num in enumerate(nums):
            b = target-num
            if (b in result):
                return [result[b],i]
            result[num]=i;