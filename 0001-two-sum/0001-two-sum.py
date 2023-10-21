class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # creating a  hashmap for storing the values
        hashmap = {}

        for number in range(len(nums)):
            compliment = target - nums[number]
            if compliment in hashmap:
                return [hashmap[compliment], number]
            
            hashmap[nums[number]] = number


        # if not found
        return []
        