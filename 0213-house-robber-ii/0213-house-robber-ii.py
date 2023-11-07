class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        #    [1, 2, 3, 4, 1]
        #i -> 0  1  2  3  4 
        # ans = max(rob from 0 to 3, rob from 1 to 4)
        return max(self.houseRobber(nums[1:]), self.houseRobber(nums[:-1]))

    def houseRobber(self, arr: List[int]) -> int:
        # [rob1, rob2, n, n + 1, ....]
        #        rob1  rob2   
        rob1, rob2 = 0, 0

        for n in arr:
            newRob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
        