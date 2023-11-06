class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # if t is an empty string
        if t == "":    
            return ""
        # creating 2 hashmaps for storing the count of letters in both s and t
        countT, window = {}, {}

        # now we can get the count of letters in the string t.
        for letter in t:
            countT[letter] = 1 + countT.get(letter, 0)

        # declaring 2 variables have and need
        have, need = 0, len(countT)

        # result variables
        res, resLen = [-1, -1], float("inf")    # as we need to find minimum so we used +infinity

        # left pointer
        left = 0

        # iterating through the s string
        for right in range(len(s)):
            # we populate its count in countS hashmap
            letter = s[right]
            window[letter] = 1 + window.get(letter, 0)

            # now if the letter is required letter and the count is same, it means  we have a new required letter
            if letter in countT and window[letter] == countT[letter]:
                have += 1

            # now while we have, have == need, we have to find a minimum window
            while have == need:
                # current window size ⇒ (right - left + 1) 
                if (right - left + 1) < resLen:
                    # we update both res as well as resLen
                    res = [left, right]
                    resLen = (right - left + 1)    # the current window

                # at this point we need to move our left pointer towards right to find the minimum window
                # pop from the left of our window
                window[s[left]] -= 1

                # update the have count too
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

        left, right = res  # this will be our final window
        return s[left: right + 1] if resLen != float("inf") else ""

        