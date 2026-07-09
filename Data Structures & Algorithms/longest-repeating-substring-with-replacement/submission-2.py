class Solution:
    def slidingWindow(self, s, a, k):
        left, right = 0, 0
        maxlen, replace = 0, 0
        while right < len(s):
            if s[right] != a and replace >= k:
                while s[left] == a:
                    left += 1
                replace -= 1
                left += 1
            if s[right] != a:
                replace += 1
            maxlen = max(maxlen, right - left + 1)
            
            right += 1
        return maxlen


    def characterReplacement(self, s: str, k: int) -> int:
        alphabets = set(s)
        ans = 0
        for i in alphabets:
            ans = max(ans, self.slidingWindow(s, i, k))
        return ans


        