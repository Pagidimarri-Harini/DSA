class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        duplicateset = set()
        n = len(nums)
        for i in range(0, n):
            if nums[i] in duplicateset:
                return True
            duplicateset.add(nums[i])
            if len(duplicateset) > k:
                duplicateset.remove(nums[i-k])

            
        return False
            
            
        