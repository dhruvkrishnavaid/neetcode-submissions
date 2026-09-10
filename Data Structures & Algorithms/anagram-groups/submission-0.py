class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        for s in strs:
            sk = tuple(sorted(s))
            d.setdefault(sk, []).append(s)
        return list(d.values())