class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitcount = defaultdict(int)
        left = 0
        maxlen = 0
        for right in range(len(fruits)):
            fruitcount[fruits[right]] += 1
            while len(fruitcount) > 2:
                fruitcount[fruits[left]] -= 1
                if fruitcount[fruits[left]] == 0:
                    del fruitcount[fruits[left]]
                left += 1
            maxlen = max(maxlen, right - left + 1)
        return maxlen
        