class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        if not len(nums):
            return 0
        c = 1
        d = 1
        l = len(nums)-2
        i = 0
        while True:
            if not i <= l:
                break
            if nums[i] + 1 == nums[i + 1]:
                d += 1
            else:
                d = 1
            if d > c:
                c = d
            i += 1
        return c