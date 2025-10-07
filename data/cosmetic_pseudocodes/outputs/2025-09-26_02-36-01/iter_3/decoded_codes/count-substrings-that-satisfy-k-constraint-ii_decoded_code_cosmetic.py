from typing import List

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        length_val = len(s)
        zero_prefix = [0] * (length_val + 1)
        one_prefix = [0] * (length_val + 1)

        for idx in range(length_val):
            zero_prefix[idx + 1] = zero_prefix[idx] + (1 if s[idx] == '0' else 0)
            one_prefix[idx + 1] = one_prefix[idx] + (1 if s[idx] == '1' else 0)

        def count_valid_substrings(l: int, r: int) -> int:
            total = 0
            pos = l
            while pos <= r:
                low, high = pos, r + 1
                while low < high:
                    middle = (low + high) // 2
                    zero_diff = zero_prefix[middle + 1] - zero_prefix[pos]
                    one_diff = one_prefix[middle + 1] - one_prefix[pos]
                    if zero_diff <= k or one_diff <= k:
                        low = middle + 1
                    else:
                        high = middle
                last_valid = low - 1
                if last_valid >= pos:
                    total += last_valid - pos + 1
                pos += 1
            return total

        output_list = []
        for query_pair in queries:
            left_bound, right_bound = query_pair
            output_list.append(count_valid_substrings(left_bound, right_bound))

        return output_list