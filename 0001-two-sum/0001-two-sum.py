class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating a hashset to store the unique values from nums
        nums_hs = {}

        # iterating over nums.
        for number_idx in range(len(nums)):
            complement = target - nums[number_idx]
            # check whether this complement exists in the nums_hs
            if complement in nums_hs:
                return [nums_hs[complement], number_idx]

            # if complement does not exist in the nums_hs, add its index to the nums_hs
            nums_hs[nums[number_idx]] = number_idx

        
        # at last return empty list if not found
        return []

        