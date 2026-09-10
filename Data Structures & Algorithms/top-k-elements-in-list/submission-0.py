class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        c = dict()
        for i in nums:
            c.setdefault(i, 0)
            c[i] += 1
        res = []
        x = 0
        while x < k:
            z = max(c, key=c.get)
            res.append(z)
            c.pop(z)
            x += 1
        return res