class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        
        s = [i for i in s if i.isalpha() or i.isnumeric()]
        j = len(s) - 1
        while i < j:
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True
        