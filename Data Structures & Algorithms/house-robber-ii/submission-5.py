class Solution:
    def maxamount(self, nums,dp, s, n):
        for i in range(n,s-1,-1):
            take = nums[i] + dp[i+2]
            notake = dp[i+1]
            dp[i] = max(take, notake)
        return dp

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [0] * (n+2)
        dp2 = [0] * (n+2)

        val1 = self.maxamount(nums, dp1, 0, n-2)[0]
        val2 = self.maxamount(nums, dp2, 1, n-1)[1]
        print(dp1, dp2)
        return max(val1, val2)

        