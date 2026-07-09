class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currsum = 0
        profit = 0
        for i in range(1,len(prices)):
            currsum = max(0, currsum + (prices[i] - prices[i-1]))
            profit = max(currsum, profit)
        return profit
        