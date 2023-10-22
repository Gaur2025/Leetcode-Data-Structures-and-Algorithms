class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # sort the list
        nums.sort()

        for idx, val in enumerate(nums):
            # if 2 consecutive elemnts are same, we need to continue
            if idx > 0 and val == nums[idx - 1]:
                continue

            # 2-pointer approach to get sum
            left, right = idx + 1, len(nums) - 1
            while left < right:
                threeSum = val + nums[left] + nums[right]

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    # now we need to also find more combinations that sum upto 0. So we need to increment left
                    left += 1
                    # but we also need to check that it is not same as previous left element
                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1

        return res

        