class Solution:
    def countSubstrings(self, s: str) -> int:
        # we can satrt with a letter in s, and move outwards (towards left and right)
        res = 0

        for i in range(len(s)):
            # for odd length substrings
            l, r = i, i

            # no out of bound rules: l >= 0 and r < len(s)
            # palindrome check: s[l] == s[r]
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1

            # for even length substrings
            l, r = i, i + 1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                res += 1
                l -= 1
                r += 1

        return res

            