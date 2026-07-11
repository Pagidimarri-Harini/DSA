class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or j < 0 or i > n-1 or j > m-1 or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            xdir = [1,0,-1,0]
            ydir = [0,1,0,-1]
            for k in range(4):
                dfs(grid, i+xdir[k], j+ydir[k])
            
        count = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    count += 1
                    dfs(grid, i, j)
                    
        return count
        