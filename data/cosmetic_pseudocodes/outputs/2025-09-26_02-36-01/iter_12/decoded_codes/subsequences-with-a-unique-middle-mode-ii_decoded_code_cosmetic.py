from collections import defaultdict

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD_VALUE = 10**9 + 7
        result_accumulator = 0
        prefix_counts = defaultdict(int)
        suffix_counts = defaultdict(int)

        for element in nums:
            suffix_counts[element] += 1

        def combinations_of_two(x):
            return x * (x - 1) // 2 if x >= 2 else 0

        cross_term_1 = 0
        cross_term_2 = 0
        prefix_squared_sum = 0  # declared but never used in original pseudocode
        suffix_squared_sum = 0
        for freq in suffix_counts.values():
            suffix_squared_sum += freq * freq
        cross_term_3 = 0

        n = len(nums)
        for idx in range(n):
            current_val = nums[idx]

            val_suffix_count = suffix_counts[current_val]
            val_prefix_count = prefix_counts[current_val]

            squared_suffix_minus_one = (val_suffix_count - 1) * (val_suffix_count - 1)
            squared_prefix = val_prefix_count * val_prefix_count

            cross_term_1 += val_prefix_count * (-val_suffix_count * val_suffix_count + squared_suffix_minus_one)
            cross_term_2 -= squared_prefix
            suffix_squared_sum -= val_suffix_count * val_suffix_count
            suffix_squared_sum += squared_suffix_minus_one
            cross_term_3 -= val_prefix_count

            suffix_counts[current_val] = val_suffix_count - 1

            left_length = idx
            right_length = n - idx - 1

            comb_left = combinations_of_two(left_length)
            comb_right = combinations_of_two(right_length)

            result_accumulator += comb_left * comb_right

            left_remain = left_length - val_prefix_count
            right_remain = right_length - suffix_counts[current_val]

            result_accumulator -= combinations_of_two(left_remain) * combinations_of_two(right_remain)

            cross_term_1_adj = cross_term_1 - val_prefix_count * val_suffix_count * val_suffix_count
            cross_term_2_adj = cross_term_2 - val_suffix_count * squared_prefix
            cross_term_3_adj = cross_term_3 - squared_prefix
            suffix_sq_adj = suffix_squared_sum - val_suffix_count * val_suffix_count
            cross_term_3_val = cross_term_3 - val_prefix_count * val_suffix_count
            prefix_remaining = left_remain
            suffix_remaining = right_remain

            # Use integer division as much as possible, but some terms may be inherently floats
            # so we convert carefully
            term1 = cross_term_3_val * val_prefix_count * (right_length - val_suffix_count) + cross_term_1_adj * (-val_prefix_count)
            term2 = cross_term_3_val * val_suffix_count * (left_length - val_prefix_count) + cross_term_2_adj * (-val_suffix_count)
            term3 = ((cross_term_3_adj - prefix_remaining) * val_suffix_count * (right_length - val_suffix_count)) / 2
            term4 = ((suffix_sq_adj - suffix_remaining) * val_prefix_count * (left_length - val_prefix_count)) / 2

            result_accumulator -= term1
            result_accumulator -= term2
            result_accumulator -= term3
            result_accumulator -= term4

            result_accumulator %= MOD_VALUE

            cross_term_1 += val_suffix_count * val_suffix_count
            cross_term_2 += val_suffix_count * (-squared_prefix + (val_prefix_count + 1) * (val_prefix_count + 1))
            cross_term_3 += -squared_prefix + (val_prefix_count + 1) * (val_prefix_count + 1)
            cross_term_3 -= squared_prefix  # Adjust cross_term_3_adj according to pseudocode (though cross_term_3_adj not used after)
            cross_term_3 += val_suffix_count

            prefix_counts[current_val] = val_prefix_count + 1

        return result_accumulator % MOD_VALUE