class Solution:
    def helper(self, nums, i, ans, res):
        res.append(ans)
        # print(i, ans)
        if i == len(nums):
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j-1]:
                continue 
            self.helper(nums, j+1, ans + [nums[j]], res)
        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        return self.helper(nums, 0, [], res)
        