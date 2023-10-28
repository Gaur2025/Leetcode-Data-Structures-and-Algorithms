class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        This function is responsible for returning the number of islands present in a given grid.
        Approach: We can just start with a grid element, and if it is an island then we can check 
                if the island is present in its adjacent position.
                Since we need to check at different levels, we can use BFS.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        # to store whether we have visited an island or not, we can use set()
        visited = set()

        islands = 0

        # Creating the BFS function
        def bfs(r, c):
            # creating a queue.
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()     # popleft removes and returns the first element.
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                        c in range(cols) and
                        grid[r][c] == "1" and
                        (r, c) not in visited):
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    # We will perform BFS
                    bfs(r, c)
                    islands += 1

        return islands

        