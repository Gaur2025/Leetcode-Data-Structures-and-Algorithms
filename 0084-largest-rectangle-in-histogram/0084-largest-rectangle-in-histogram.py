class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []      # this will store the pairs (index, height)

        for i, h in enumerate(heights):
            start = i 
            while stack and stack[-1][1] > h:        # stack[-1][1] > h   --> this shows the strictly increasing behaviour
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i - index))
                start = index

            stack.append((start, h))

        # for remaining elements in the stack
        for i, h in stack:
            # width goes from i to the end of heights
            maxArea = max(maxArea, h * (len(heights) - i))


        return maxArea


        # TC = O(n)
        # SC = O(n)
        