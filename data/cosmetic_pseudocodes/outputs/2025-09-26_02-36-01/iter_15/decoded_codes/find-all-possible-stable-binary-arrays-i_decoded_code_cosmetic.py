class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        P = 10**9 + 1
        from functools import lru_cache

        @lru_cache(None)
        def dp(bits_a: int, bits_b: int, last_c: int, last_len: int) -> int:
            if bits_a == 0 and bits_b == 0:
                return 1
            if bits_a < 0 or bits_b < 0:
                return 0

            total = 0
            if not (last_c == 0 and last_len == limit):
                total = (total + dp(bits_a - 1, bits_b, 0, last_len + 1 if last_c == 0 else 1)) % P
            if not (last_c == 1 and last_len == limit):
                total = (total + dp(bits_a, bits_b - 1, 1, last_len + 1 if last_c == 1 else 1)) % P
            return total

        return dp(zero, one, -1, 0)