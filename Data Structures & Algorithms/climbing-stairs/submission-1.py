class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * n
        def countStairs(n, dp):
            if n <= 1:
                return 1
            if dp[n-1] != 0:
                return dp[n-1]
            dp[n-1] = countStairs(n-1, dp) + countStairs(n-2, dp)
            return dp[n-1]
        return countStairs(n, dp)

        