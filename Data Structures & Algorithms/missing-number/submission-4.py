class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        lst = nums.sort()
        counter = 0
        for i in range(n): 
            if i != nums[i]: 
                return int(i)
            else: 
                counter += 1
        
        if counter == n: 
            return n
