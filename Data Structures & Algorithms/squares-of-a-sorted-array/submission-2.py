class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        count = len([i for i in nums if i < 0])
        n = len(nums)
        nums = [abs(i) for i in nums] + [0]*count
        i = n - 1
        j = 0
        curr = n + count - 1
        while j < count and i >= count:
            if nums[j] > nums[i]:
                nums[curr] = nums[j]
                j += 1
                curr -= 1
            else:
                nums[curr] = nums[i]
                i -= 1
                curr -= 1
        while j < count:
            nums[curr] = nums[j]
            j += 1
            curr -= 1
            
        return [i*i for i in nums[count:]]





        