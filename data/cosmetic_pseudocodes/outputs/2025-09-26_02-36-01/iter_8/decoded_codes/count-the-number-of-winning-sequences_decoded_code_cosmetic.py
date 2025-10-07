class Solution:
    def countWinningSequences(self, s: str) -> int:
        mod = 10**9 + 7
        d = {"F": 0, "W": 1, "E": 2}

        from functools import lru_cache

        def calc(q: int, r: int) -> int:
            t = (q == r)
            if t:
                return 0
            if q < r:
                if (q == 0 and r == 2):
                    return 1
                else:
                    return -1
            u = (q == 2 and r == 0)
            if u:
                return -1
            else:
                return 1

        @lru_cache(None)
        def dfs(p: int, m: int, n: int) -> int:
            if len(s) - p > m:
                pass
            else:
                return 0

            if p >= len(s):
                return 1 if m < 0 else 0

            w = 0
            v = 0
            while v <= 2:
                if v == n:
                    v += 1
                    continue
                x = dfs(p + 1, m + calc(d[s[p]], v), v)
                w = (w + x) % mod
                v += 1
            return w

        ans = dfs(0, 0, -1)
        dfs.cache_clear()
        return ans