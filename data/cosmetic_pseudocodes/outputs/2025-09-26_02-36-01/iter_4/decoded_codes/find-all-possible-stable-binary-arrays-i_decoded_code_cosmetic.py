class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO_VALUE = 1_000_000_001

        from functools import lru_cache

        @lru_cache(None)
        def dp(remaining_zeros: int, remaining_ones: int, previous_char: int, run_length: int) -> int:
            if remaining_zeros == 0 and remaining_ones == 0:
                return 1
            if remaining_zeros < 0 or remaining_ones < 0:
                return 0

            tally = 0
            # Try to add zero if allowed
            if previous_char != 0 or run_length < limit:
                new_run_length_0 = run_length + 1 if previous_char == 0 else 1
                tally += dp(remaining_zeros - 1, remaining_ones, 0, new_run_length_0)
                tally %= MODULO_VALUE

            # Try to add one if allowed
            if previous_char != 1 or run_length < limit:
                new_run_length_1 = run_length + 1 if previous_char == 1 else 1
                tally += dp(remaining_zeros, remaining_ones - 1, 1, new_run_length_1)
                tally %= MODULO_VALUE

            return tally

        return dp(zero, one, -1, 0)