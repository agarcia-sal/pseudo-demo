from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        m = len(s)
        zero_prefix_accumulator = [0] * (m + 1)
        one_prefix_accumulator = [0] * (m + 1)

        def build_prefix_arrays() -> None:
            for idx in range(m):
                zero_flag = 1 if s[idx] == '0' else 0
                one_flag = 1 if s[idx] == '1' else 0
                zero_prefix_accumulator[idx + 1] = zero_prefix_accumulator[idx] + zero_flag
                one_prefix_accumulator[idx + 1] = one_prefix_accumulator[idx] + one_flag

        build_prefix_arrays()

        def determine_count(start_index: int, end_index: int) -> int:
            total_substrings = 0
            current_start = start_index

            while current_start <= end_index:
                low_bound = current_start
                high_bound = end_index + 1

                # Binary search for max end index of substring starting at current_start 
                # with zeros or ones count ≤ k
                while low_bound < high_bound:
                    mid_point = (low_bound + high_bound) // 2
                    zero_count_substring = zero_prefix_accumulator[mid_point + 1] - zero_prefix_accumulator[current_start]
                    one_count_substring = one_prefix_accumulator[mid_point + 1] - one_prefix_accumulator[current_start]
                    if zero_count_substring <= k or one_count_substring <= k:
                        low_bound = mid_point + 1
                    else:
                        high_bound = mid_point

                max_end = low_bound - 1
                if max_end >= current_start:
                    total_substrings += (max_end - current_start + 1)
                current_start += 1

            return total_substrings

        output_results = []
        for left_range, right_range in queries:
            result_value = determine_count(left_range, right_range)
            output_results.append(result_value)

        return output_results