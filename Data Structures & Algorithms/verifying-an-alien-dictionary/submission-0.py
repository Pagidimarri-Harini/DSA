class Solution:


    def isAlienSorted(self, words: List[str], order: str) -> bool:
        aliendict = {k: v for v, k in enumerate(order)}
        print(aliendict)
        for i in range(len(words) - 1):
            first, second = words[i], words[i+1]

            for j in range(len(first)):
                if j == len(second):
                    return False
                if first[j] != second[j]:
                    if aliendict[first[j]] > aliendict[second[j]]:
                        return False
                    break
        return True
                    

         
        