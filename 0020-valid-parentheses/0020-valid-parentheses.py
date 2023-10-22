class Solution:
    def isValid(self, s: str) -> bool:
        stack = []    # to store the char from str. 
        openToClose = {")":"(", "]":"[", "}":"{"}

        # Now let us check each char from the given str
        for char in s:
            # if char is in openToClose i.e., it is among close brackets.
            if char in openToClose:
                # if stack is not empty and last element in stack is open bracket
                if stack and stack[-1] == openToClose[char]:
                    stack.pop()
                else:
                    return False

            else:          # if char is not in openToClose i.e., is is an open bracket. So we add it to our stack
                stack.append(char)

        # at last if stack is not empty return True
        return True if not stack else False
        