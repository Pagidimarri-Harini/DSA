class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a%b
        return a
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        a, b = len(str1), len(str2)
        gcd = self.gcd(a, b)
        return str1[:gcd]
        