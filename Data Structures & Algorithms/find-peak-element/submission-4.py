class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        n = len(nums) - 1
        if len(nums) == 1:
            return 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid-1] < nums[mid] and mid < n and nums[mid] > nums[mid+1]:
                    return mid
            elif mid < n and nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid - 1
            
            
        return mid
            


        