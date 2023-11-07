class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 [1, 2, 3]

        # we can have 2 variables to last and second last element (these both will be 1)
        one, two = 1, 1

        for i in range(n - 1):
            # one will come one place back, and two will go to one's place
            temp = one
            one = one + two
            two = temp

        # at last we return one
        return one
