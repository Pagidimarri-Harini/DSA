class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def helper(s, res, temp):
            if s == "":
                res.append(temp[:])
                return 
            
            
            for i in range(len(s)):
                ans = s[:i+1]
                if ans == ans[::-1]:
                    helper(s[i+1:], res, temp + [ans])
            return res
        res = []
        res = helper(s,res,[])
        return res
        