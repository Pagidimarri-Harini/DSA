class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)
        def calcCost(cost, i):
            if i >= len(cost):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(calcCost(cost,i+1), calcCost(cost,i+2))
            return dp[i]
        return min(calcCost(cost, 0), calcCost(cost, 1))

        