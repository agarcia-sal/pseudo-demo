from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: List[int], k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n_token = len(s)
        prefix_variableA = [0] * (n_token + 1)
        prefix_variableB = [0] * (n_token + 1)

        for index_marker in range(n_token):
            temp_zero = prefix_variableA[index_marker]
            temp_one = prefix_variableB[index_marker]
            char_value = s[index_marker]
            is_zero_value = 1 if char_value == 0 else 0
            is_one_value = 1 if char_value == 1 else 0
            prefix_variableA[index_marker + 1] = temp_zero + is_zero_value
            prefix_variableB[index_marker + 1] = temp_one + is_one_value

        def count_valid_substrings(l: int, r: int) -> int:
            accumulator_count = 0
            pos_counter = l
            while pos_counter <= r:
                left_bound = pos_counter
                right_bound = r + 1
                while left_bound < right_bound:
                    mid_pos = (left_bound + right_bound) // 2
                    zero_range = prefix_variableA[mid_pos + 1] - prefix_variableA[pos_counter]
                    one_range = prefix_variableB[mid_pos + 1] - prefix_variableB[pos_counter]
                    if zero_range <= k or one_range <= k:
                        left_bound = mid_pos + 1
                    else:
                        right_bound = mid_pos
                final_end = left_bound - 1
                if final_end >= pos_counter:
                    accumulator_count += (final_end - pos_counter + 1)
                pos_counter += 1
            return accumulator_count

        output_list = []
        for left_query, right_query in queries:
            value_from_call = count_valid_substrings(left_query, right_query)
            output_list.append(value_from_call)

        return output_list