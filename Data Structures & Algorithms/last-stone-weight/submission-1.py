class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            top = -heapq.heappop(stones)
            top1 = -heapq.heappop(stones)
            if top - top1 != 0:
                heapq.heappush(stones, top1 - top)
        if stones:
            return -stones[0]
        return 0

        