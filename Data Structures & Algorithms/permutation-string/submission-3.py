class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqcount = sum(map(ord, s1))

        k = len(s1)
        currfreq = sum(map(ord, s2[:k]))
        for i in range(k, len(s2)):
            print(s2[i-k:i])
            if currfreq == freqcount and set(s1) == set(s2[i-k:i]):
                return True

            currfreq += ord(s2[i])
            currfreq -= ord(s2[i-k])
        i = len(s2)
        print(i)
        if currfreq == freqcount and set(s1) == set(s2[i-k:i]):
                return True
        
        return False


        