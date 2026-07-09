class Solution:
    def trap(self, height: List[int]) -> int:
        leftmaxis = []
        rightmaxis = []
        currmax = -1
        for i in height:
            leftmaxis.append(currmax)
            currmax = max(currmax, i)
        currmax = -1
        for i in height[::-1]:
            rightmaxis.append(currmax)
            currmax = max(currmax, i)
        rightmaxis = rightmaxis[::-1]
        waterfill = []
        for i in range(len(height)):
            waterfill.append(min(leftmaxis[i], rightmaxis[i]) - height[i])
        waterfill = [i for i in waterfill if i > 0]
        return sum(waterfill)

            
        