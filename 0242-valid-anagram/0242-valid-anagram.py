class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # As s and t may contain duplicate value, we need to create hashmaps.
        countS, countT = {}, {}

        # popluate hashmaps with key as letter, and value as its count.
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # 0 is the default value
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Now check for key, values in countS and countT
        for letter in countS:
            if (countS[letter] != countT.get(letter, 0)):
                return False

        return True

        