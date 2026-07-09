
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = bucket = [[] for _ in range(len(nums) + 1)]
        count = Counter(nums)
        for key, val in count.items():
            bucket[val].append(key)

        ans = []
        print(bucket)
        for i in bucket[::-1]:
            if i != []:
                ans.extend(i)
                k -= len(i)
            if k == 0:
                break
        return ans

        