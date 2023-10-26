class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashSet = set()     # to store the unique values from nums

        for i in range(len(nums)):     # O(n)
            if nums[i] in hashSet:
                return nums[i]

            # add this to the hashSet
            hashSet.add(nums[i])

        # if no duplicate found
        return -1
        
        