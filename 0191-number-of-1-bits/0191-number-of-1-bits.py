class Solution:
    def hammingWeight(self, n: int) -> int:
        # we can just check the modulo of n. if it is 1 we can add it ot res. Shift by 1 bit after every check
        res = 0
        while n:
            # 1101 % 2 = 1, 1010 % 2 = 0 (Modulo 2 just returns the last bit)
            res += n % 2    # n % 2 will either give 1 or 0. so we can just add this to res
            # shift n by 1 bit
            n = n >> 1

        return res
        