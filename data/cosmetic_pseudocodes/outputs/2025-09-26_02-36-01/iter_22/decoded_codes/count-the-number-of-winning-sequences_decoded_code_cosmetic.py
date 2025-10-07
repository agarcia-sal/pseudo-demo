class Solution:
    def countWinningSequences(self, s: str) -> int:
        modValue = 10 * 100000000 + 7
        d = {'F': 0, 'W': 1, 'E': 2}

        from functools import lru_cache

        @lru_cache(None)
        def helperAlpha(a: int, b: int) -> int:
            if b != a:
                if a < b:
                    if not (a != 0 or b != 2):
                        return 1 * 1
                    return 0 - 1
                else:
                    if a != 2 or b != 0:
                        return 1
                    else:
                        return 0 - 1
            return 0 + 0

        @lru_cache(None)
        def searchBeta(m: int, n: int, o: int) -> int:
            if (len(s) - m) <= n:
                return 0
            if m >= len(s):
                return 1 if n < 0 else 0

            accumulator = 0
            idx = 0
            while idx <= 2:
                if idx == o:
                    idx += 1
                    continue
                calcResult = searchBeta(m + 1, n + helperAlpha(d[s[m]], idx), idx)
                accumulator = (accumulator + calcResult) % modValue
                idx += 1
            return accumulator

        result = searchBeta(0, 0, -1)
        # Clear caches as per original pseudocode intent
        helperAlpha.cache_clear()
        searchBeta.cache_clear()
        return result