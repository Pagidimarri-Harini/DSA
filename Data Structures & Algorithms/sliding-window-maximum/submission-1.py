class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = []
        windowstart, count = 0, 0
        ans = []
        for i in range(len(nums)):
            if count < k:
                while stack and nums[stack[-1]] < nums[i]:
                    stack.pop()
                stack.append(i)
                count += 1
            if count == k:
                while stack and stack[0] < windowstart:
                    stack.pop(0)

                ans.append(nums[stack[0]])
                count -= 1
                windowstart += 1
        return ans
                

        