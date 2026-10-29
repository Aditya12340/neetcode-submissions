
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        hm = {}

        m = len(nums)

        for i in nums:
            if i not in hm:
                hm[i] = 1
            else:
                hm[i] += 1

        x = max(hm, key=hm.get)
        y = hm[x]

        count = 0

        for i in range(m - 1):
            if nums[i] == x:
                count += 1

            left = i + 1
            right = m - left

            if count * 2 > left and (y - count) * 2 > right:
                return i

        return -1
