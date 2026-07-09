class Solution:
    def compress(self, chars: List[str]) -> int:
        lastchar = ""
        j = 0
        count = 0
        for i in range(len(chars)):
            if chars[i] == lastchar:
                    count += 1
            else:
                if count == 1:
                    j += 1
                x = len(str(count))
                if count > 1:   
                    chars[j+1:j+x+1]= list(str(count))
                    j = j + x +1
                chars[j] = chars[i]
                count = 1
                lastchar = chars[i]
 
        if count > 1:
            x = len(str(count))
            print(j+1, j+x+1)
            chars[j+1:j+x+1]= list(str(count))
            j = j + x+1
        if count == 1:
            j += 1
        return len(chars[:j])

        