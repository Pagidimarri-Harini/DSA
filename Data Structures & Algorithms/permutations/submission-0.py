class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums, res, ans, n):
            if len(ans) == n:
                res.append(ans)
                return
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:], res, ans + [nums[i]], n)
            return res
        n = len(nums)
        return helper(nums, res, [], n)

        