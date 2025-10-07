from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 10**9 + 1

        @lru_cache(None)
        def dp(curr_zero_count: int, curr_one_count: int, prev_char: int, run_len: int) -> int:
            if curr_zero_count == 0 and curr_one_count == 0:
                return 1
            if curr_zero_count < 0 or curr_one_count < 0:
                return 0

            sum_result = 0

            can_append_zero = not (prev_char == 0 and run_len >= limit)
            can_append_one = not (prev_char == 1 and run_len >= limit)

            if can_append_zero:
                next_run_length = run_len + 1 if prev_char == 0 else 1
                sum_result = (sum_result + dp(curr_zero_count - 1, curr_one_count, 0, next_run_length)) % modulus

            if can_append_one:
                next_run_length = run_len + 1 if prev_char == 1 else 1
                sum_result = (sum_result + dp(curr_zero_count, curr_one_count - 1, 1, next_run_length)) % modulus

            return sum_result

        return dp(zero, one, -1, 0)