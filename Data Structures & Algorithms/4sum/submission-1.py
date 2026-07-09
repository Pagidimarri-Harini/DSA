class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        nums.sort()
        # print(nums)
        for l in range(n-3):
            if l > 0 and nums[l] == nums[l-1]:
                    continue
            for i in range(l+1,n-2):
                j = i + 1
                k = n - 1
                if i > l+1 and nums[i] == nums[i-1]:
                    continue
                while j < k:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        ans.append([nums[i], nums[j], nums[k],nums[l]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1

                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1

                    elif total < target:
                        j += 1
                    else:
                        k -= 1

        return ans
        