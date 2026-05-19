class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_arr = len(nums)
        product_arr = []

        product = 1
        zeroexist = 0

        for num in nums:
            if num == 0:
                zeroexist += 1
            else:
                product *= num


        if zeroexist >= 2:
            return [0] * len_arr


        if zeroexist == 1:
            for num in nums:
                if num == 0:
                    product_arr.append(product)
                else:
                    product_arr.append(0)
            return product_arr

        for num in nums:
            product_arr.append(product // num)

        return product_arr