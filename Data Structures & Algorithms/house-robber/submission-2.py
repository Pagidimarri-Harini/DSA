class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def calcAmt(nums, i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            left = nums[i] + calcAmt(nums, i+2)
            right = calcAmt(nums, i+1)
            dp[i] = max(left, right)
            return dp[i]
        return max(calcAmt(nums, 0), calcAmt(nums, 1))
        