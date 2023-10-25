class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        We need to find the substring. We can use set to store the duplicate char in given s.
        The Sliding Window approach can be used for solving this problem.
        """
        charSet = set()    # This will be used to store unique char from s
        p1 = 0             # Saving the first pointer at start of s
        res = 0            # we will be storing the length of the largest substring

        # we will iterate on s.
        for p2 in range(len(s)):
            # while char at p2 is already present in the charSet. Then it is duplicate char.
            # We remove it from charSet
            while s[p2] in charSet:
                charSet.remove(s[p1])
                p1 += 1               # we move a step ahead at p1
            # if element at p2 is not duplicate we will store it in charSet.
            charSet.add(s[p2])

            # update the res
            res = max(res, (p2 - p1) + 1)      # +1 because we have 0-based indexing


        return res

        