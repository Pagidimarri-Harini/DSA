class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n, m = len(grid), len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    fresh += 1
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        time = 0
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                x, y = q.popleft()
                for i in range(4):
                    newx = x + dir[i][0]
                    newy = y + dir[i][1]
                    if newx < 0 or newy < 0 or newx > n-1 or newy > m-1 or grid[newx][newy] != 1:
                        continue
                    grid[newx][newy] = 2
                    fresh -= 1
                    q.append((newx,newy))
            time += 1
        return time if fresh == 0 else -1



        