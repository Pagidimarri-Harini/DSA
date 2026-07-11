class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        MAX_SIZE = 2**31 - 1
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        while q:
            x,y = q.popleft()
            for i in range(4):
                newi = dir[i][0] + x
                newj = dir[i][1] + y
                if newi < 0 or newj < 0 or newi > n-1 or newj > m-1 or grid[newi][newj] != MAX_SIZE:
                    continue
                grid[newi][newj] = grid[x][y] + 1
                q.append((newi,newj)) 



        