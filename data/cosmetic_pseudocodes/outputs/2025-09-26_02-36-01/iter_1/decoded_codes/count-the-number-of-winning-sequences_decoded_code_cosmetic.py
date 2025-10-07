class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        def calc(a: int, b: int) -> int:
            if a == b:
                return 0
            elif a < b:
                if a == 0 and b == 2:
                    return 1
                else:
                    return -1
            else:
                if a == 2 and b == 0:
                    return -1
                else:
                    return 1

        from functools import cache

        @cache
        def dfs(index: int, balance: int, last_move: int) -> int:
            if len(s) - index <= balance:
                return 0
            if index >= len(s):
                return 1 if balance < 0 else 0

            total = 0
            for move in range(3):
                if move == last_move:
                    continue
                updated_balance = balance + calc(d[s[index]], move)
                total = (total + dfs(index + 1, updated_balance, move)) % mod
            return total

        result = dfs(0, 0, -1)
        dfs.cache_clear()
        return result