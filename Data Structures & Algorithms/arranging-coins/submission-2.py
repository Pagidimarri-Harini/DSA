class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 0
        r = n
        while l <= r:
            mid = (l + r) //2
            if mid * (mid + 1) //2 <= n:
                l = mid + 1
            else:
                r = mid - 1
        return r

        