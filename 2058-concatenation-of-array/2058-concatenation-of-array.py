class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy()

        left, right = 0, len(nums)

        while left < (len(nums)):
            ans.append(nums[left])
            left += 1
            right += 1

        return ans

        