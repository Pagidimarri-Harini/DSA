class Solution:
    def helper(self, board, word, i, j, ind):
        if ind == len(word):
            return True
        if i == len(board) or j == len(board[0]) or i < 0 or j < 0 or word[ind] != board[i][j]:
            return False
        xdir = [0,1,-1,0]
        ydir = [1,0,0,-1]
        for k in range(4):
            temp = board[i][j]
            board[i][j] = "#"
            if self.helper(board, word,i + xdir[k], j+ydir[k], ind+1):
                return True
            board[i][j] = temp
        return False
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j, 0):
                    return True
        return False


        