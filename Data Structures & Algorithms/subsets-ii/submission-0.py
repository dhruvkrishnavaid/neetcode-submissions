class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []

        def b(p, s):
            if s == len(nums):
                r.append(list(p))
                return

            p.append(nums[s])
            b(p, s + 1)
            p.pop()

            ns = s + 1
            while ns < len(nums) and nums[ns] == nums[s]:
                ns += 1
            b(p, ns)

        b([], 0)
        return r