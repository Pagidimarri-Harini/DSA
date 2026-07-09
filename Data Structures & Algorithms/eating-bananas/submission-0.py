class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            k = (left + right)//2
            count = 0
            for p in piles:
                count += ((p//k) + (p%k != 0))
            if count <= h:
                right = k - 1
            else:
                left = k + 1
        return left
        