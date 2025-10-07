from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        ZERO_CONST = 0
        ONE_CONST = 1

        length_s = len(s)

        prefix_count_zeros = [ZERO_CONST] * (length_s + ONE_CONST)
        prefix_count_ones = [ZERO_CONST] * (length_s + ONE_CONST)

        for index_i in range(length_s):
            prefix_count_zeros[index_i + ONE_CONST] = prefix_count_zeros[index_i] + (ONE_CONST if s[index_i] == '0' else ZERO_CONST)
            prefix_count_ones[index_i + ONE_CONST] = prefix_count_ones[index_i] + (ONE_CONST if s[index_i] == '1' else ZERO_CONST)

        def count_valid_substrings(l: int, r: int) -> int:
            total_count = ZERO_CONST

            def binary_search_valid(end_point: int) -> int:
                low_bound = end_point
                high_bound = r + ONE_CONST

                while low_bound < high_bound:
                    mid_point = (low_bound + high_bound) // 2
                    zero_segment = prefix_count_zeros[mid_point + ONE_CONST] - prefix_count_zeros[end_point]
                    one_segment = prefix_count_ones[mid_point + ONE_CONST] - prefix_count_ones[end_point]
                    if zero_segment <= k or one_segment <= k:
                        low_bound = mid_point + ONE_CONST
                    else:
                        high_bound = mid_point
                return low_bound - ONE_CONST

            outer_idx = l
            while outer_idx <= r:
                max_valid_end = binary_search_valid(outer_idx)
                if max_valid_end >= outer_idx:
                    total_count += max_valid_end - outer_idx + ONE_CONST
                outer_idx += ONE_CONST

            return total_count

        output_list = []
        for query in queries:
            l_val, r_val = query[ZERO_CONST], query[ONE_CONST]
            output_list.append(count_valid_substrings(l_val, r_val))

        return output_list