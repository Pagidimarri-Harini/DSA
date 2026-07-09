class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[mid]:
                if nums[right] > nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid

        return nums[left]

        