class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        hash1 = [0] * 26
        hash2 = [0] * 26
        k = len(s1)
        for i in s1:
            hash1[ord(i) - 97] += 1
        for i in range(len(s2)):
            if hash1 == hash2:
                return True
            hash2[ord(s2[i])-97] +=1
            if i >= k:
                hash2[ord(s2[i-k])-97] -=1
        return hash1 == hash2
        


        