class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # step 1: sort the input array
        # need a visited list. 
        # two ptr approach
        nums = sorted(nums)
        res = []
        temp = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue # this is checking apriori
            target = -nums[i]
            l, r = i + 1, len(nums) -1 
            while l < r: 
                if nums[l] + nums[r] > target: 
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([-target,nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
            continue
        
        return res
        








'''
Say you have: 
[0, -2, 4, 3 , -2]: 
0 + twosum(-2, 4, 3 , -2) -> res[]



'''



