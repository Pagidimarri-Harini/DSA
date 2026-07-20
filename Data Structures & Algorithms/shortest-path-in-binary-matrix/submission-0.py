class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0]) 
        q = deque()
        if grid[0][0] == 0:
            q.append((0,0,1))
        distance = 0
        grid[0][0] = 1
        while q:
            nodei, nodej, value = q.popleft()
            if (nodei, nodej) == (n-1, m-1):
                return value
            dirs = [(-1,-1), (-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
            for i in range(8):
                newx, newy = nodei + dirs[i][0], nodej + dirs[i][1]
                if newx < 0 or newy < 0 or newx > n - 1 or newy > m - 1 or grid[newx][newy] == 1:
                    continue
                grid[newx][newy] = 1
                q.append((newx, newy, value + 1))
                
        return -1
        