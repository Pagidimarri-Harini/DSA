import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        while k > 0:
            first = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(math.sqrt(first)))
            k -= 1

        return abs(sum(gifts))

        