class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        while i < len(nums):
            if nums[i] % 2 == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                i += 1
        return nums
        