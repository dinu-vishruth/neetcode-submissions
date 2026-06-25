class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        f={}
        for i,num in enumerate(nums):
            need=target-num
            if need in f:
                return [f[need],i]
            f[num]=i
