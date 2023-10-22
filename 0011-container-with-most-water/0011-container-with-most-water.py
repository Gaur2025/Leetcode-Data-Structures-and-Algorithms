class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## 2 iteration approach (TC = O(n^2), SC = O(1))
        # maxWater = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         volume = min(height[i], height[j])*(j-i)
        #         maxWater = max(maxWater, volume)

        # return maxWater

        ## 2 pointer approach (TC = O(n/2), SC = O(1))
        maxWater = 0

        # defining both pointers
        left, right = 0, len(height) - 1

        while left < right:
            area = min(height[left], height[right]) * abs(left - right)
            maxWater = max(area, maxWater)

            # update the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
        


        