class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        # [1, 2, 3, 4, 5, 6, 7]
        #  l        m        r

        while left <= right:
            # mid index
            mid = (left + right) // 2

            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid

        return -1

        