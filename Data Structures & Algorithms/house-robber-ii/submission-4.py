class Solution:
    def maxamount(self, nums, dp, i, n):
        if i > n:
            return 0
        # print(nums)
        if dp[i] != -1:
            return dp[i]
        take = nums[i] + self.maxamount(nums, dp, i+2,n)
        notake = self.maxamount(nums, dp, i+1, n)
        dp[i] = max(take, notake)
        return dp[i]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [-1] * n
        dp2 = [-1] * n
        return max(self.maxamount(nums, dp1, 0, n-2), self.maxamount(nums, dp2, 1, n-1))

        