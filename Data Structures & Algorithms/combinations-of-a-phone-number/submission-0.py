class Solution:
    def helper(self,digits, phone, ans, temp):
        if digits == "":
            if temp != "":
                ans.append(temp)
            return
        for j in phone[digits[0]]:
            self.helper(digits[1:], phone, ans, temp + j)
        
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        self.helper(digits,phone,ans, "")
        return ans


        