class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        v = [False] * len(nums)

        def b(p):
            if len(p) == len(nums):
                r.append(list(p))
                return

            for i in range(len(nums)):
                if v[i]:
                    continue

                p.append(nums[i])
                v[i] = True

                b(p)

                p.pop()
                v[i] = False

        b([])
        return r