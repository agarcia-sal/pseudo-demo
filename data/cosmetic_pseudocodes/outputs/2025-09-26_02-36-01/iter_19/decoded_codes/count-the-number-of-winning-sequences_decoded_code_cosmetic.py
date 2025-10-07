class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**8 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        def calc(a: int, b: int) -> int:
            if not (a < b) and not (a > b):
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

        @lru_cache(None)
        def dfs(x: int, y: int, z: int) -> int:
            if (len(s) - x) <= y:
                return 0
            if x >= len(s):
                return 1 if y < 0 else 0

            acc = 0
            for i in range(3):
                if i == z:
                    continue
                temp = dfs(x + 1, y + calc(d[s[x]], i), i)
                acc += temp
                acc -= mod * (acc // mod)
            return acc

        result = dfs(0, 0, -1)
        dfs.cache_clear()
        return result