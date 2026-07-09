class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashtable = defaultdict(int)
        newtable = defaultdict(int)
        formed, required = 0, 0
        for i in t:
            if hashtable[i] == 0:
                required += 1
            hashtable[i] += 1
        left = 0
        right = 0
        ans = ""
        
        minlength = sys.maxsize
        while right < len(s):
            print(left, right)
            if hashtable[s[right]] > 0:
                newtable[s[right]] += 1
                if newtable[s[right]] == hashtable[s[right]]:
                    formed += 1
                
            while formed == required:

                if right - left + 1 < minlength:
                    minlength = right - left + 1
                    ans = s[left:right + 1]
                if hashtable[s[left]] > 0: 
                    if newtable[s[left]] == hashtable[s[left]]:
                        formed -= 1
                    newtable[s[left]] -= 1
                    
                left += 1

            right += 1

        return ans
            
        