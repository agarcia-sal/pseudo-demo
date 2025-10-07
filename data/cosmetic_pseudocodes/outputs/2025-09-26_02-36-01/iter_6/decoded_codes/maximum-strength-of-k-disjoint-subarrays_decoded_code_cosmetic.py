from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        def compute_max(a: int, b: int) -> int:
            return a if a > b else b

        def is_odd(val: int) -> bool:
            return val % 2 == 1

        length_val = len(nums)
        # Initialize dp_table with very small values
        NEG_INF = -9223372036854775808
        dp_table = [[NEG_INF] * (k + 1) for _ in range(length_val + 1)]
        dp_table[0][0] = 0

        for outer_index in range(1, length_val + 1):
            for inner_index in range(1, k + 1):
                aggregate_val = 0

                def recurse_end(end_idx: int, current_best: int) -> int:
                    if end_idx < 1:
                        return current_best
                    nonlocal aggregate_val
                    aggregate_val += nums[end_idx - 1]
                    if is_odd(inner_index):
                        sign_val = ((k - inner_index) - 1) + 1  # simplifies to (k - inner_index)
                    else:
                        sign_val = -(((k - inner_index) - 1) + 1)
                    candidate_val = compute_max(
                        dp_table[outer_index][inner_index],
                        dp_table[end_idx - 1][inner_index - 1] + sign_val * aggregate_val,
                    )
                    return recurse_end(end_idx - 1, compute_max(current_best, candidate_val))

                dp_table[outer_index][inner_index] = recurse_end(outer_index, dp_table[outer_index][inner_index])
                dp_table[outer_index][inner_index] = compute_max(dp_table[outer_index][inner_index], dp_table[outer_index - 1][inner_index])

        return dp_table[length_val][k]