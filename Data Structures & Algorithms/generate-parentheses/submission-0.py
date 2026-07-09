class Solution:
    def helper(self, n, res, ans, opened, closed):
        if len(ans) == 2*n:
            res.append(ans)
            return
        if opened < n:
            self.helper(n, res, ans + "(", opened+1, closed)
        if opened > closed:
            self.helper(n, res, ans + ")", opened, closed+1)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, res, "", 0, 0)
        return res
        
        