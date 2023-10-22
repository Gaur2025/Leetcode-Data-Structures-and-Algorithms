class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach 1. (TC = O(n), SC = O(n))

        # create a valid_str list with lowercase and alphanumeric values only.
        temp = []
        for char in s:
            if (ord(char) >= ord("A")) and (ord(char) <= ord("Z")):
                temp.append(char.lower())
            elif (ord(char) >= ord("a")) and (ord(char) <= ord("z")):
                temp.append(char)
            elif (ord(char) >= ord("0")) and (ord(char) <= ord("9")):
                temp.append(char)
            else:    # for non-alphanumeric
                continue

        # till this point we have a list containing all the lower case alphanumeric values from str s.

        # creating 2 pointers --> left and right to check whether left and right character are same.
        left = 0
        right = len(temp) - 1

        while left < right:
            if (temp[left] != temp[right]):
                return False
            else:
                left += 1
                right -= 1
        
        # if all goes fine. Then given input is palindrome
        return True


        