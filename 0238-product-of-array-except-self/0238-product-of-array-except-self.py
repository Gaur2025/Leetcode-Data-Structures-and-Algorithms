class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # Brute force
    #     res = []

    #     for i in range(len(nums)):
    #         product = 1
    #         for j in range(len(nums)):
    #             if j == i:
    #                 continue

    #             # get the product
    #             product *= nums[j]

    #         # append the product to the result
    #         res.append(product)

    #     return res
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # TC = O(n), SC = O(1)
        res = [1 for _ in range(len(nums))]

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        