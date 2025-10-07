from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        length_s = len(s)
        zero_prefix_arr = [0] * (length_s + 1)
        one_prefix_arr = [0] * (length_s + 1)

        for idx in range(length_s):
            current_zero_val = 1 if s[idx] == '0' else 0
            current_one_val = 1 if s[idx] == '1' else 0
            zero_prefix_arr[idx + 1] = zero_prefix_arr[idx] + current_zero_val
            one_prefix_arr[idx + 1] = one_prefix_arr[idx] + current_one_val

        def count_valid_substrings(l: int, r: int) -> int:
            total_count = 0
            start_pos = l
            while start_pos <= r:
                low, high = start_pos, r + 1
                while low < high:
                    mid_val = (low + high) // 2
                    zeros_sub_count = zero_prefix_arr[mid_val + 1] - zero_prefix_arr[start_pos]
                    ones_sub_count = one_prefix_arr[mid_val + 1] - one_prefix_arr[start_pos]
                    if zeros_sub_count <= k or ones_sub_count <= k:
                        low = mid_val + 1
                    else:
                        high = mid_val
                substring_end = low - 1
                if substring_end >= start_pos:
                    length_contrib = substring_end - start_pos + 1
                    total_count += length_contrib
                start_pos += 1
            return total_count

        answers = []
        for left_bound, right_bound in queries:
            current_result = count_valid_substrings(left_bound, right_bound)
            answers.append(current_result)

        return answers