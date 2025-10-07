class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD_CONST = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(rem_zeros: int, rem_ones: int, prev_char: int, run_len: int) -> int:
            if rem_zeros == 0 and rem_ones == 0:
                return 1
            if rem_zeros < 0 or rem_ones < 0:
                return 0

            acc = 0

            if not (prev_char == 0 and run_len >= limit):
                next_run_length = run_len + 1 if prev_char == 0 else 1
                acc = (acc + dp(rem_zeros - 1, rem_ones, 0, next_run_length)) % MOD_CONST

            if not (prev_char == 1 and run_len >= limit):
                next_run_length = run_len + 1 if prev_char == 1 else 1
                acc = (acc + dp(rem_zeros, rem_ones - 1, 1, next_run_length)) % MOD_CONST

            return acc

        return dp(zero, one, -1, 0)