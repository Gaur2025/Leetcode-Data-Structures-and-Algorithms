class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using Floyd's algorithm

        # finding 1st intersection of slow and fast pointer
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Now we create one new pointer at beginning
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        