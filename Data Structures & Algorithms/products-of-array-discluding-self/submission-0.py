class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = []
        rightproduct = []
        l, r = 1,1
        n = len(nums)
        for i in range(len(nums)):
            l *= nums[i]
            r *= nums[n - i - 1]
            leftproduct.append(l)
            rightproduct.append(r)
        rightproduct = rightproduct[::-1]
        ans = []
        # print(leftproduct, rightproduct)
        for i in range(n):
            if i == 0:
                ans.append(rightproduct[i+1])
            elif i == n - 1:
                ans.append(leftproduct[i-1])
            else:
                ans.append(leftproduct[i-1] * rightproduct[i+1])
        return ans

        