class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        n, m = len(nums1), len(nums2)
        left, right = 0, n

        while left <= right:
            part1 = (left + right) // 2 
            part2 = (n + m + 1) // 2 - part1
            l1 = float('-inf') if part1 == 0 else nums1[part1-1]
            l2 = float('-inf') if part2 == 0 else nums2[part2-1]
            r1 = float('inf') if part1 == n else nums1[part1]
            r2 = float('inf') if part2 == m else nums2[part2]

            if l1 <= r2 and l2 <= r1:
                if (n+m)%2 == 0:
                    return (max(l1,l2) + min(r1,r2))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                right = part1 - 1
            else:
                left = part1 + 1

        

        
        