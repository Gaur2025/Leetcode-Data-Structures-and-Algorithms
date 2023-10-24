class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # try to find th evalue in the sorted half
        ans = float("inf")
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if (nums[left] <= nums[mid]):
                # it means left half is sorted. 
                ans = min(ans, nums[left])
                # now move to the other half
                left = mid + 1
            else:
                # right half is sorted
                ans = min(ans, nums[mid])
                # move to the other half (left)
                right = mid - 1

        return ans
        