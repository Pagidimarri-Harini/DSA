class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        end, start= 0, 0
        ans = 0
        while end < len(s):
            
            if s[end] in hash:
                
                ans = max(ans, end - start)
                start = max(start, hash[s[end]] + 1)
                hash[s[end]] = end
                end += 1

            else:
                hash[s[end]] = end
                end += 1
        ans = max(ans, end - start)

        return ans
        