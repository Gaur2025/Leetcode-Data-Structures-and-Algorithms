class Solution:
    def trap(self, height: List[int]) -> int:
        # 2-pointer approach

        # water will be stored if left and right noundary exists.
        maxWater = 0
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]

        while left < right:
            if leftMax < rightMax:   # means left boundary is less than right
                left += 1
                leftMax = max(leftMax, height[left])
                # water stored till here will be max left boundary minus this position's height
                maxWater += leftMax - height[left]
            else:                    # means right boundary is less than left
                right -= 1
                rightMax = max(rightMax, height[right])
                # water stored after this will be max right boundary minus this position's height
                maxWater += rightMax - height[right]

        return maxWater
        