class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1. Only add open parenthesis if openN < n
        2. Only add closed parenthesis if closedN < openN
        3. Stop when openN == closedN == n
        """
        stack, res = [], []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))    # convert everything in stack into a string and append it to the stack
                return
            
            if openN < n:    
                # we add the open parenthesis
                stack.append("(")
                # again backtrack
                backtrack(openN + 1, closedN)
                # remove the appended parenthesis from the stack
                stack.pop()

            if closedN < openN:    
                # we add the closed parenthesis
                stack.append(")")
                # again backtrack
                backtrack(openN, closedN + 1)
                # remove the appended parenthesis from the stack
                stack.pop()
        
        # call the backtrack function
        backtrack(0, 0)

        return res