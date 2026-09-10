class Solution:

    def encode(self, strs: list[str]) -> str:
        e = []
        for s in strs:
            e.append(f"{len(s)}#{s}")
        return "".join(e)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j + 1
            res.append(s[i : i + l])
            i += l
        return res