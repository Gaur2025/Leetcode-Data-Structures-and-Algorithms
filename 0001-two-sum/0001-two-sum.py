class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        size = len(nums)

        for i in range(size):
            complement = target - nums[i]
            if complement in res:
                return [res[complement], i]
            
            # if complement does not exist, add the cuurent element nums[i] to res with its index as the value
            res[nums[i]] = i

        # if not found
        return []


        