class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []

        def b(p: str, o: int, c: int):
            if len(p) == 2 * n:
                r.append(p)
                return

            if o < n:
                b(p + "(", o + 1, c)

            if c < o:
                b(p + ")", o, c + 1)

        b("", 0, 0)
        return r