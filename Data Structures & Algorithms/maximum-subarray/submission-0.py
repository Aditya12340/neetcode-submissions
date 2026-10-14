class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: 
            return 0 
        if len(nums) == 1: 
            return nums[0]
        
        best = -(10**100000)
        curSum = 0 
        for i in nums: 
            curSum = max(i, curSum+i)
            best = max(curSum, best)
        return best

        