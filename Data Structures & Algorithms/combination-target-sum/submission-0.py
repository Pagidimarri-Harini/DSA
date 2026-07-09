class Solution:
    def helper(self, nums, res, target, ans):
        if target < 0 or nums == []:
            return
        if target == 0:
            res.append(ans)
            return
        # print(ans, nums)
        self.helper(nums, res, target - nums[0], ans + [nums[0]])
        self.helper(nums[1:], res, target, ans)
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        self.helper(nums, res, target, [])
        return res

        