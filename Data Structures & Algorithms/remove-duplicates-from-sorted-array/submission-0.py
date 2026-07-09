class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 1, 1
        lastappeared = nums[0]
        while i < len(nums):
            if nums[i] != lastappeared:
                nums[j] = nums[i]
                lastappeared = nums[i]
                i += 1
                j += 1
            else:
                i += 1
        return j 

        