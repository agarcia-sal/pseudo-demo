class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MODULO_VALUE = 10**9 + 1

        from functools import lru_cache

        @lru_cache(None)
        def dp(zeros_left: int, ones_left: int, last_character: int, last_run_length: int) -> int:
            if zeros_left == 0 and ones_left == 0:
                return 1
            if zeros_left < 0 or ones_left < 0:
                return 0

            result_accumulator = 0

            if last_character != 0 or last_run_length < limit:
                increment_value = dp(
                    zeros_left - 1,
                    ones_left,
                    0,
                    last_run_length + 1 if last_character == 0 else 1,
                )
                result_accumulator += increment_value
                result_accumulator %= MODULO_VALUE

            if last_character != 1 or last_run_length < limit:
                increment_value = dp(
                    zeros_left,
                    ones_left - 1,
                    1,
                    last_run_length + 1 if last_character == 1 else 1,
                )
                result_accumulator += increment_value
                result_accumulator %= MODULO_VALUE

            return result_accumulator

        return dp(zero, one, -1, 0)