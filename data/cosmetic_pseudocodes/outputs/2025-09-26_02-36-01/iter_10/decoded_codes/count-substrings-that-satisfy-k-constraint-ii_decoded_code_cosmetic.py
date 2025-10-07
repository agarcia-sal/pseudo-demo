from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        length_s = len(s)
        zeros_prefix = [0] * (length_s + 1)
        ones_prefix = [0] * (length_s + 1)

        for index_counter in range(length_s):
            zeros_prefix[index_counter + 1] = zeros_prefix[index_counter] + (1 if s[index_counter] == '0' else 0)
            ones_prefix[index_counter + 1] = ones_prefix[index_counter] + (1 if s[index_counter] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            total_count = 0
            outer_start = l
            while outer_start <= r:
                binary_left = outer_start
                binary_right = r + 1
                # Binary search to find max substring end with <= k zeros or ones
                while binary_left < binary_right:
                    mean_val = (binary_left + binary_right) // 2

                    zeros_in_range = zeros_prefix[mean_val + 1] - zeros_prefix[outer_start]
                    ones_in_range = ones_prefix[mean_val + 1] - ones_prefix[outer_start]

                    if zeros_in_range <= k or ones_in_range <= k:
                        binary_left = mean_val + 1
                    else:
                        binary_right = mean_val
                max_end_index = binary_left - 1
                if max_end_index >= outer_start:
                    total_count += (max_end_index - outer_start + 1)
                outer_start += 1
            return total_count

        accumulation = []
        for current_pair in queries:
            left_bound, right_bound = current_pair
            accumulation_element = count_valid_substrings(left_bound, right_bound)
            accumulation.append(accumulation_element)

        return accumulation