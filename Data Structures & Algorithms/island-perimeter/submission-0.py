class Solution:
    def dfs(self, grid, i, j, n, m, visited):
        
        if i < 0 or j < 0 or i > n - 1 or j > m - 1 or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        xdir = [1,0,-1,0]
        ydir = [0,1,0,-1]
        visited.add((i,j))
        perim = 0
        for dir in range(4):
            perim += self.dfs(grid,i+xdir[dir],j+ydir[dir],n,m,visited)
        
        return perim
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        xdir = [1,0,-1,0]
        ydir = [0,1,0,-1]
        visited = set()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return self.dfs(grid, i, j, n, m, visited)
                
                