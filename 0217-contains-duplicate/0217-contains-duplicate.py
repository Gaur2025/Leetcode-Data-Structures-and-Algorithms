class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach => Using a hashset to store non-duplicate values
        # TC = O(n), SC = O(n)
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            # if num not present in the hashset. We can add this to our hashset
            hashset.add(num)


        # if not found
        return False

        