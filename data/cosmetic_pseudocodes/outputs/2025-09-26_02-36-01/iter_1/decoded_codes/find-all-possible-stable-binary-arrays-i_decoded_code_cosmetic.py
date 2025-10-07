class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD_CONST = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(zeros_remaining: int, ones_remaining: int, prev_char: int, run_len: int) -> int:
            if zeros_remaining == 0 and ones_remaining == 0:
                return 1
            if zeros_remaining < 0 or ones_remaining < 0:
                return 0

            total_ways = 0

            if prev_char != 0 or run_len < limit:
                next_run = run_len + 1 if prev_char == 0 else 1
                total_ways += dp(zeros_remaining - 1, ones_remaining, 0, next_run)
                total_ways %= MOD_CONST

            if prev_char != 1 or run_len < limit:
                next_run = run_len + 1 if prev_char == 1 else 1
                total_ways += dp(zeros_remaining, ones_remaining - 1, 1, next_run)
                total_ways %= MOD_CONST

            return total_ways

        return dp(zero, one, -1, 0)