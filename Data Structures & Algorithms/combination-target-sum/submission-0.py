class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        r = []

        def b(m, p, s):
            if m == 0:
                r.append(list(p))
                return
            if m < 0:
                return

            for i in range(s, len(nums)):
                p.append(nums[i])
                b(m - nums[i], p, i)
                p.pop()

        b(target, [], 0)
        return r