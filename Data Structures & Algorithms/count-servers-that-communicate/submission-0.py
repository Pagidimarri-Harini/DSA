class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        row = [0] * n
        col = [0] * m
        for i in range(n):
            for j in range(m):
                row[i] += grid[i][j]
                col[j] += grid[i][j]
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += (row[i] > 1) or (col[j] > 1)
        return count



        
        