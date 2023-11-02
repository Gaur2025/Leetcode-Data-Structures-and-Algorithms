class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        This function is responsible for calculating the perimeter of an island.
        """
        # defining a visited set
        visited = set()

        # creating the dfs function
        def dfs(i, j):
            # base case
            if (i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0):
                return 1

            # if already visited
            if (i, j) in visited:
                return 0
        
            visited.add((i, j))
            # using recursion
            perimeter = dfs(i + 1, j)
            perimeter += dfs(i - 1, j)
            perimeter += dfs(i, j + 1)
            perimeter += dfs(i, j - 1)

            return perimeter

        

        # we need to find a land and start dfs from that place
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
