class Solution:
    def dfs(self, board, i, j, n, m):
        if i < 0 or j < 0 or i > n-1 or j > m-1 or board[i][j] == 'X' or board[i][j] == 'H':
            return
        # print(i, j)
        board[i][j] = 'H'
        xdir = [1,0,-1,0]
        ydir = [0,1,0,-1]
        for d in range(4):
            self.dfs(board, i+xdir[d], j+ydir[d], n, m)

    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        sources = []
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and board[i][j] == 'O':
                    sources.append((i,j))
        # print(sources)
        for s in sources:
            if board[s[0]][s[1]] == 'O':
                self.dfs(board, s[0], s[1], n, m)
        # print(board)
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'H':
                    board[i][j] = 'O'
        
        