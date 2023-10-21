class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to create a hashmap
        res = {}

        # iterate through all the values of nums
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in res:
                # return [complement_index_fromhashmap, current_index]
                return [res[complement], idx]


            # add values to the hashmap
            res[nums[idx]] = idx

        # if not found
        return []
        