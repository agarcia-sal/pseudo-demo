from functools import cache

class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        def calc(a: int, b: int) -> int:
            if a > b:
                if a == 2 and b == 0:
                    return -1
                else:
                    return 1
            elif a < b:
                if a == 0 and b == 2:
                    return 1
                else:
                    return -1
            else:
                return 0

        @cache
        def dfs(x: int, y: int, z: int) -> int:
            if (len(s) - x) <= y:
                return 0
            if x >= len(s):
                return 1 if y < 0 else 0

            total = 0
            for idx in range(3):
                if idx != z:
                    total += dfs(x + 1, y + calc(d[s[x]], idx), idx)
                    total %= mod
            return total

        result = dfs(0, 0, -1)
        dfs.cache_clear()
        return result