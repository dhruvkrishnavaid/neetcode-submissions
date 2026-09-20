class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []

        def b(p, s):
            if s == len(nums):
                r.append(list(p))
                return

            p.append(nums[s])
            b(p, s + 1)
            p.pop()

            b(p, s + 1)

        b([], 0)
        return r