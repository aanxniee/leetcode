class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def valid(grid, r, c):
            return r >= 0 and r < m and c >= 0 and c < n

        def island(grid, r, c):
            s = 1
            grid[r][c] = 0

            if valid(grid, r+1, c) and grid[r+1][c] == 1:
                s += island(grid, r+1, c)
            
            if valid(grid, r-1, c) and grid[r-1][c] == 1:
                s += island(grid, r-1, c)

            if valid(grid, r, c+1) and grid[r][c+1] == 1:
                s += island(grid, r, c+1)

            if valid(grid, r, c-1) and grid[r][c-1] == 1:
                s += island(grid, r, c-1)

            return s

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, island(grid, i, j))

        return max_area
