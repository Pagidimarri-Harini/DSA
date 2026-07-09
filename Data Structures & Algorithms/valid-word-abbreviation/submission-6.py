class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        aj = 0
        wj = 0
        count = ""
        while wj < len(word) and aj < len(abbr):
            print(wj, aj)
            if abbr[aj].isnumeric():
                count += abbr[aj]
                aj += 1
            
            elif abbr[aj].isalpha():
                if count != "":
                    if count[0] == "0":
                        return False
                    
                    wj += (int(count))
                    count = ""
                elif abbr[aj] != word[wj]:
                    return False
                else:
                    aj += 1
                    wj += 1

        if count != "":
            if count[0] == "0":
                return False
            wj += (int(count))
            count = ""
        print(wj)
        return wj == len(word) and aj == len(abbr)


        