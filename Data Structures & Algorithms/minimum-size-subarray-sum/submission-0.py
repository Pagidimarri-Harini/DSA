class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        currsum = 0
        count = sys.maxsize
        for right in range(len(nums)):
            currsum += nums[right]
            print(currsum)
            while currsum >= target:
                count = min(count, (right - left+1))
                currsum -= nums[left]
                left += 1
        if count == sys.maxsize:
            return 0
        return count

            
        