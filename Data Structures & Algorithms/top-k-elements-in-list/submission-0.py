class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in range(len(nums)): 
            if nums[i] in seen: 
                seen[nums[i]] += 1
            else: 
                seen[nums[i]] = 1
        temp = max(seen, key=seen.get)
        res = []
        temp = 0
        for i in range(k):
            temp = max(seen, key=seen.get)
            res.append(temp)
            seen.pop(temp)

        return res
            



        