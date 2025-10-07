class Solution:
    def countWinningSequences(self, s: str) -> int:
        MOD = 10**9 + 7
        M = {'F': 0, 'W': 1, 'E': 2}
        n = len(s)

        from functools import lru_cache

        def delta(a: int, b: int) -> int:
            if a == b:
                return 0
            if a < b:
                if a == 0 and b == 2:
                    return 1
                else:
                    return -1
            if a == 2 and b == 0:
                return -1
            else:
                return 1

        @lru_cache(None)
        def recur(p: int, q: int, r: int) -> int:
            if (n - p) <= q:
                return 0
            if p >= n:
                return 1 if q < 0 else 0

            accumulator = 0

            for m in range(3):
                if m != r:
                    step = recur(p + 1, q + delta(M[s[p]], m), m)
                    accumulator = (accumulator + step) % MOD

            return accumulator

        answer = recur(0, 0, -1)
        recur.cache_clear()
        return answer