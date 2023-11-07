class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # [10, 15, 20] 0
        # we need to reach at position 0
        # so we can start getting minimum cost from end of the list
        cost_copy = cost.copy()

        cost_copy.append(0)

        # we want to start from the 2nd last element of the list in reverse order
        for i in range(len(cost_copy) - 3, -1, -1):
            # cost_copy[i] = min(cost_copy[i] + cost_copy[i + 1], cost_copy[i] + cost_copy[i + 2])
            cost_copy[i] += min(cost_copy[i + 1], cost_copy[i + 2])

        # at last we return the minimum of first and second value from the list coz we know we have atleast 2 elements in the list
        return min(cost_copy[0], cost_copy[1])
        