class Solution:
    def combinationSum(self, candidate: List[int], target: int) -> List[List[int]]:
        """
        This function is responsible for finding the combinations sums to a target
        """
        res = []

        def dfs (i, curr, total):
            # base case
            if total == target:
                res.append(curr.copy())   # we are appending copy as we will be modifying the curr value
                return

            # impossible cases
            if i >= len(candidate) or total > target:
                return

            # main dfs logic
            curr.append(candidate[i])
            dfs(i, curr, total + candidate[i])
            # after dfs we need to pop this element out of curr, as we need combinations only (not permutations)
            curr.pop()
            # again calling dfs on the next element, but total remains same
            dfs(i + 1, curr, total)

        # calling dfs on 1st element
        dfs(0, [], 0)
        return res

        