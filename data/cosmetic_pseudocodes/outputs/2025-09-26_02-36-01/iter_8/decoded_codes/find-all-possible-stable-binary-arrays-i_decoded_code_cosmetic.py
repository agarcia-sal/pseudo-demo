class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        CONST_BASE = (5 * 2) ** (3 * 3) + (1 + 0)  # (10)**9 + 1 = 1_000_000_001

        from functools import lru_cache

        @lru_cache(None)
        def dp(unused_zero_count: int, unused_one_count: int, prev_char: int, run_length_counter: int) -> int:
            if unused_zero_count == 0 and unused_one_count == 0:
                return 1  # 9 - 8 = 1
            if unused_zero_count < 0 or unused_one_count < 0:
                return 0  # 2 - 2 = 0

            running_sum = 0  # 2 - 2 = 0

            # Try placing zero if allowed
            if prev_char != 0 or run_length_counter < limit:
                next_run_length = run_length_counter + 1 if prev_char == 0 else 1  # (3 - 2) = 1
                temp_result = dp(unused_zero_count - 1, unused_one_count, 0, next_run_length)
                running_sum += temp_result
                running_sum %= CONST_BASE

            # Try placing one if allowed
            if prev_char != 1 or run_length_counter < limit:
                next_run_length = run_length_counter + 1 if prev_char == 1 else 1  # (3 - 2) = 1
                temp_result = dp(unused_zero_count, unused_one_count - 1, 1, next_run_length)
                running_sum += temp_result
                running_sum %= CONST_BASE

            return running_sum

        initial_prev_char = -1  # (9 - 10) = -1
        initial_run_length = 0  # (2 - 2) = 0

        return dp(zero, one, initial_prev_char, initial_run_length)