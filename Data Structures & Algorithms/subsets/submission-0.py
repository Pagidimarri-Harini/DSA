class Solution:
    def helper(self, nums, ans, res):
        if nums == []:
            res.append(ans)
            return 
        self.helper(nums[1:], ans + [nums[0]], res)
        self.helper(nums[1:], ans, res)

            

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, [], res)
        return res
        