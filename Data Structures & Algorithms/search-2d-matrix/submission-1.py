class Solution:
    def BinarySearch(self,nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix)-1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                return self.BinarySearch(matrix[mid],target)
        return False

        