class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustdict = defaultdict(int)
        for i in trust:
            trustdict[i[1]] += 1
            trustdict[i[0]] -= 1
            print(trustdict)
        for i in range(1, n+1):
            if trustdict[i] == n-1:
                return i
        return -1

        