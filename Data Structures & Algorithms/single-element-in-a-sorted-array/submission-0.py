class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            print(l, r)
            mid = (l + r) // 2
            if mid > 0 and (nums[mid] == nums[mid - 1] and mid % 2 != 0) or (nums[mid] != nums[mid -1] and mid % 2 == 0):
                l = mid + 1
            else:
                r = mid - 1
        return nums[l - 1]
            

        