class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # we need 2 different sets to capture the cells to which water can flow
        pacific = set()
        atlantic = set()
        
        # defining our rows and cols
        nrows = len(heights)
        ncols = len(heights[0])

        # water will flow towards the cell if value of cell is greater or equal than preHeight
        # this is an dfs function
        def waterFlow(r, c, visited, prevHeight):
            
            # base case (flow condition + out of bound rules + already visited)
            if (r < 0 or r == nrows or c < 0 or c == ncols or heights[r][c] < prevHeight or (r, c) in visited):
                return

            visited.add((r, c))
            # apply dfs in each adjacent direction
            waterFlow(r + 1, c, visited, heights[r][c])
            waterFlow(r - 1, c, visited, heights[r][c])
            waterFlow(r, c + 1, visited, heights[r][c])
            waterFlow(r, c - 1, visited, heights[r][c])
        

        # row boundary
        for row in range(nrows):
            # towards the pacific ocean
            waterFlow(row, 0, pacific, heights[row][0])
            # towards the atlantic ocean
            waterFlow(row, ncols - 1, atlantic, heights[row][ncols - 1])


        # col boundary
        for col in range(ncols):
            # towards the pacific ocean
            waterFlow(0, col, pacific, heights[0][col])
            # towards the atlantic ocean
            waterFlow(nrows - 1, col, atlantic, heights[nrows - 1][col])    


        res = []
        for row in range(nrows):
            for col in range(ncols):
                if (row, col) in pacific and (row, col) in atlantic:
                    res.append([row, col])

        return res

        