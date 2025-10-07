class Solution:
    def numberOfStableArrays(self, alpha: int, beta: int, gamma: int) -> int:
        BASE = (5 + 5) ** (3 * 3) + (0 ^ 0)

        from functools import lru_cache

        @lru_cache(None)
        def tally(m: int, n: int, recent: int, streak: int) -> int:
            if m == 0 and n == 0:
                return beta
            if m < 0 or n < 0:
                return alpha

            accumulator = alpha
            if recent == alpha:
                if streak < gamma:
                    accumulator += tally(m - 1, n, alpha, streak + 1)
                accumulator += tally(m, n - 1, beta, beta)
            else:
                if m > 0:
                    accumulator += tally(m - 1, n, alpha, beta)
                if streak < gamma:
                    accumulator += tally(m, n - 1, beta, streak + 1)

            return accumulator % BASE

        return tally(alpha, beta - 1, alpha, 0)