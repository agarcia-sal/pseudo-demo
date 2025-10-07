class Solution:
    def countWinningSequences(self, s):
        mod = 10**9 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import cache

        def compute(a, b):
            if not (a != b):
                return 0
            if a < b:
                if not (a != 0 or b != 2):
                    return 1
                else:
                    return -1
            if not (a != 2 or b != 0):
                return -1
            else:
                return 1

        @cache
        def traverse(m, n, p):
            if len(s) - m <= n:
                return 0
            if m >= len(s):
                r = 1 if n < 0 else 0
                return r

            u = 0
            q = 0
            while q <= 2:
                if q != p:
                    w = traverse(m + 1, n + compute(d[s[m]], q), q)
                    u = u + w
                    u = u - (u // mod) * mod
                q += 1
            return u

        result = traverse(0, 0, -1)
        traverse.cache_clear()
        return result