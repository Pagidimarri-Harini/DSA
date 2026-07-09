class Solution:
    def helper(self, candidates, target, ans, res, i):
        if target == 0:
            res.append(ans)
            return
        if target < 0 or i == len(candidates):
            return
        # print(i, target, ans)
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j-1]:
                continue
            self.helper(candidates, target-candidates[j], ans+[candidates[j]], res, j+1)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        print(candidates)
        self.helper(candidates, target,[], res, 0)
        return res

        