class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        r = []

        def b(t, p, s):
            if t == 0:
                r.append(list(p))
                return
            if t < 0:
                return

            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i - 1]:
                    continue

                if candidates[i] > t:
                    break
                p.append(candidates[i])
                b(t - candidates[i], p, i + 1)
                p.pop()

        b(target, [], 0)
        return r
