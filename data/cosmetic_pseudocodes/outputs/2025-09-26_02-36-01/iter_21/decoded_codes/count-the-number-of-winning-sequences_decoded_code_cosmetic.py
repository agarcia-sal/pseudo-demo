from functools import lru_cache

class Solution:
    def countWinningSequences(self, s):
        d = {"F": 0, "W": 1, "E": 2}
        mod = 10**9 + 7

        def calc(x, y):
            # Recursive helper is redundant as it returns c if a == b,
            # else continues infinitely (no progress), so directly handled below.

            alpha, beta, gamma = 0, 1, -1

            if x == y:
                return alpha + alpha  # 0

            if not (x >= y):
                if not (x != 0) and not (y != 2):
                    return beta
                else:
                    return gamma

            if x == 2 and y == 0:
                return gamma
            else:
                return beta

        @lru_cache(None)
        def dfs(i, j, k):
            def conditionCheck():
                return (len(s) - i) <= j

            def cond2():
                return i >= len(s)

            if conditionCheck():
                return 0
            if cond2():
                return 1 if j < 0 else 0

            tmpRes = 0
            idx = 0
            while True:
                if idx == 3:
                    break
                if idx != k:
                    a1 = i + 1
                    a2 = calc(d[s[i]], idx)
                    a3 = j + a2
                    r1 = dfs(a1, a3, idx)
                    tmpRes += r1
                    if tmpRes >= mod or tmpRes <= -mod:
                        tmpRes %= mod
                idx += 1

            return tmpRes % mod

        resFinal = dfs(0, 0, -1)
        dfs.cache_clear()
        return resFinal