class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we can start at an char and go outwards from it, to check for the palindrome
        res = ""
        resLen = 0

        for i in range(len(s)):
            # for odd length
            l, r = i, i

            # no out of bound rules: l >= 0 and r <= len(s)
            # palindrome rule:  s[l] == s[r]
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                # check for max value
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1

            # for even length
            l, r = i, i + 1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                # check for max value
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1

                l -= 1
                r += 1
            
        return res
        