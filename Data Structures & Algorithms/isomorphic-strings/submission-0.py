class Solution:
    def positions(self, s: str) -> dict:
        d = dict()
        for i, a in enumerate(s):
            d.setdefault(a, [])
            d[a].append(i)
        return d

    def isIsomorphic(self, s: str, t: str) -> bool:
        sd = self.positions(s)
        td = self.positions(t)

        return list(sd.values()) == list(td.values())