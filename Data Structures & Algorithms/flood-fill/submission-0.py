class Solution:
    def dfs(self,image, color1, color2, i, j, n, m):
        if i < 0 or j < 0 or i > n-1 or j > m-1 or image[i][j] != color1:
            return
        image[i][j] = color2
        xdir = [1,0,-1,0]
        ydir = [0,1,0,-1]
        for k in range(4):
            self.dfs(image, color1, color2,xdir[k] + i, ydir[k] + j,n, m)
        

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        self.dfs(image, image[sr][sc],color, sr, sc, len(image), len(image[0]))
        return image

        