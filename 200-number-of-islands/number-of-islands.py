class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        """
        traverse through the matrix
        when you reach a cell that is 1, dfs it to mark that island as visited
        increment island count

        dfs: 
            1. check if cell is valid (within bounds, is a 1)
            2. mark it as visited, set to -1
            3. call dfs in all 4 directions
        """
        
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def dfs(grid, r, c):

            if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != "1":
                return

            grid[r][c] = "-1"

            dfs(grid, r+1, c)
            dfs(grid, r-1, c)
            dfs(grid, r, c+1)
            dfs(grid, r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(grid, r, c)
                    islands += 1
        
        return islands