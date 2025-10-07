from functools import lru_cache

class Solution:
    def countWinningSequences(self, s):
        mod = 10**9 + 7
        d = {"F": 0, "W": 1, "E": 2}

        def calc(a, b):
            if a == b:
                return 0
            elif a < b:
                if a == 0 and b == 2:
                    return 1
                else:
                    return -1
            elif a == 2 and b == 0:
                return -1
            else:
                return 1

        @lru_cache(None)
        def dfs(p, q, r):
            lengthS = len(s)
            if (lengthS - p) <= q:
                return 0
            if p >= lengthS:
                return 1 if q < 0 else 0

            accumulator = 0
            for index in range(3):
                if index == r:
                    continue
                currentCharValue = d[s[p]]
                increment = calc(currentCharValue, index)
                nextP = p + 1
                nextQ = q + increment
                accumulator += dfs(nextP, nextQ, index)
                accumulator %= mod

            return accumulator

        result = dfs(0, 0, -1)
        dfs.cache_clear()
        return result