class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if 0 in nums:
            z = []
            for p in nums:
                if p != 0:
                    z += [p]
            if not z or len(nums) - len(z) > 1:
                return [0] * len(nums)
            d = 1
            for i in z:
                d *= i
            a = [d] * len(nums)
            for i, x in zip(range(len(a)), nums):
                if x != 0:
                    a[i] = 0
            return a

        d = 1
        for i in nums:
            d *= i
        a = [d] * len(nums)
        for i, x in zip(range(len(a)), nums):
            a[i] //= x

        return a
