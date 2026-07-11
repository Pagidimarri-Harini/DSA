class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j,count):
            if i < 0 or j < 0 or i > n-1 or j > m-1 or grid[i][j] == 0:
                return count
            grid[i][j] = 0
            xdir = [1,0,-1,0]
            ydir = [0,1,0,-1]
            count += 1
            for k in range(4):
                count = dfs(grid, i+xdir[k], j+ydir[k], count)
            return count
            
        maxarea = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    maxarea = max(maxarea, dfs(grid, i, j,0))
        return maxarea
        