class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Binary search approach.
        # check if target is at mid
        # if not check if left half is sorted and change left and right according to availability in left half.
        # also check if right half is sorted and change left and right according to availability in right half

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # check if left half is sorted
            if nums[left] <= nums[mid]:
                # now check whether target is present in this left half
                # left<------target------->mid
                if (nums[left] <= target and nums[mid] >= target):
                    # change the value of right
                    right = mid - 1
                else:
                    left = mid + 1
            else: 
                # means right half is sorted
                # lets check whether target is present in the right half
                # mid<---------target------->right
                if (nums[mid] <= target and nums[right] >= target):
                    # change the value of left
                    left = mid + 1
                else:
                    right = mid - 1
            
        # if not found 
        return -1
        