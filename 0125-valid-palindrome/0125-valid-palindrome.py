class Solution:
    def isPalindrome(self, s: str) -> bool:
        # using python methods
        newStr = ""

        for char in s:
            if char.isalnum():
                newStr += char.lower()

        # check whether reverse is same as original
        return (newStr == newStr[::-1])
        