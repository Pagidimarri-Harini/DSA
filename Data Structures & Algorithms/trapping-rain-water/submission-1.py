class Solution:
    def trap(self, height: List[int]) -> int:
        leftmaxis = []
        rightmaxis = []
        leftmax, rightmax = -1, -1
        i, j = 0, len(height) - 1
        while i < len(height) and j >= 0:
            leftmaxis.append(leftmax)
            leftmax = max(leftmax, height[i])
            rightmaxis.append(rightmax)
            rightmax = max(height[j], rightmax)
            i += 1
            j -= 1

        rightmaxis = rightmaxis[::-1]
        waterfill = []
        for i in range(len(height)):
            waterfill.append(min(leftmaxis[i], rightmaxis[i]) - height[i])
        print(waterfill)
        waterfill = [i for i in waterfill if i > 0]
        return sum(waterfill)

            
        