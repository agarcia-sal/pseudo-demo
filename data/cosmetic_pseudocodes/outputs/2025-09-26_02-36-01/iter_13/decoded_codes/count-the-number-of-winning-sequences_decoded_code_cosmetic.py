class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import cache

        def computeDiff(a: int, b: int) -> int:
            if a == b:
                return 0
            if a < b:
                if a == 0 and b == 2:
                    return 1
                return -1
            else:
                if a == 2 and b == 0:
                    return -1
                return 1

        @cache
        def visit(pos: int, balance: int, prev: int) -> int:
            if (len(s) - pos) <= balance:
                return 0
            if pos >= len(s):
                return 1 if balance < 0 else 0

            total = 0
            for index in range(3):
                if index != prev:
                    val = computeDiff(d[s[pos]], index)
                    total = (total + visit(pos + 1, balance + val, index)) % mod
            return total

        result = visit(0, 0, -1)
        visit.cache_clear()
        return result