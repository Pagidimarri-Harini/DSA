class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def helper(s, res, temp, ans):
            print(ans, s, temp)
            # if ans != "":
            #     if ans != ans[::-1]:
            #         return
            #     temp = temp + [ans]
            if s == "":
                res.append(temp[:])
                return 
            
            
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    helper(s[i+1:], res, temp + [s[:i+1]], s[:i+1])
            return res
        res = []
        res = helper(s,res,[], "")
        return res
        