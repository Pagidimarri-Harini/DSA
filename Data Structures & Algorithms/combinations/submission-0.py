class Solution:
    def helper(self, nums, res, ans, k):
        if len(ans) == k:
            res.append(ans)
            return
        if nums == []:
            return
        
        self.helper(nums[1:], res, ans + [nums[0]], k)
        self.helper(nums[1:], res, ans, k)
        return res
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i+1 for i in range(n)]
        return self.helper(nums, [], [], k)

        