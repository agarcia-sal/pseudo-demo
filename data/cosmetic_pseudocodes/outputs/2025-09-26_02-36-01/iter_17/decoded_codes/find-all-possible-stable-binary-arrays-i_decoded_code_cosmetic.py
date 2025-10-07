class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        A = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(a: int, b: int, c: int, d: int) -> int:
            if a == 0 and b == 0:
                return 1
            if a < 0 or b < 0:
                return 0

            x = 0
            if c != 0 or d < limit:
                x += dp(a - 1, b, 0, d + 1 if c == 0 else 1)
                x %= A
            if c != 1 or d < limit:
                x += dp(a, b - 1, 1, d + 1 if c == 1 else 1)
                x %= A
            return x

        return dp(zero, one, -1, 0)