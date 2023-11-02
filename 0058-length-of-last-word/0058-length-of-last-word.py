class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s) == 1 and s[0] != ' ':
            return 1

        right = len(s) - 1
        while s[right] == ' ':
            right -= 1

        ans = 0
        while (right >= 0 and s[right] != ' '):
            ans += 1
            right -= 1

        return ans
        