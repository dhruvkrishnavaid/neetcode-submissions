class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int, s: int) -> bool:
            if s == len(word):
                return True

            if (i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[s]):
                return False

            temp = board[i][j]
            board[i][j] = '*'

            found = (
                dfs(i + 1, j, s + 1) or
                dfs(i - 1, j, s + 1) or
                dfs(i, j + 1, s + 1) or
                dfs(i, j - 1, s + 1)
            )

            board[i][j] = temp
            return found

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True

        return False