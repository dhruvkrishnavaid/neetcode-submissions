# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        p = pairs.copy()
        l = len(p)
        i = 0
        res = []
        if len(p) > 0:
            res.append(list(p))
        for i in range(1, len(p)):
            key = p[i].key
            pp = p[i]
            j = i - 1

            while j >= 0 and key < p[j].key:
                p[j + 1] = p[j]
                j -= 1
            p[j + 1] = pp

            res.append(list(p))

        return res