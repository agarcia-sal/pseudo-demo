class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        def calc(x: int, y: int) -> int:
            if x == y:
                return 0
            if x < y:
                if x == 0 and y == 2:
                    return 1
                else:
                    return -1
            if x == 2 and y == 0:
                return -1
            else:
                return 1

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, k: int) -> int:
            if len(s) - i <= j:
                return 0
            if i >= len(s):
                return 1 if j < 0 else 0
            res = 0
            for l in range(3):
                if l == k:
                    continue
                res += dfs(i + 1, j + calc(d[s[i]], l), l)
                res %= mod
            return res

        ans = dfs(0, 0, -1)
        dfs.cache_clear()
        return ans