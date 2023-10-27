class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20] 0

        costCopy = cost.copy()

        for i in range(len(costCopy) - 3, -1, -1):
            costCopy[i] += min(costCopy[i + 1], costCopy[i + 2])

        return min(costCopy[0], costCopy[1])
        