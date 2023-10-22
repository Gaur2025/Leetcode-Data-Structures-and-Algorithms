class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Minimum value will be the minimum of new value being added and top value of minStack if minStack is non empty at this point.
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # this should be in O(1) time. So, we can return the top of minStack
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()