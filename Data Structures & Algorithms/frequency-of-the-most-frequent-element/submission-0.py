class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, 0
        currsum = 0
        maxlen = 0
        n = len(nums)
        for right in range(n):
            currsum += nums[right]
            if ((right - left+1) * nums[right]) - currsum > k:
                currsum -= nums[left]
                left += 1
        return n - left
        

        