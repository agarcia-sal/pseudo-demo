from math import floor
from typing import List, Tuple


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        n_var = len(s)

        zero_prefix = [0] * (n_var + 1)
        one_prefix = [0] * (n_var + 1)

        for idx_var in range(n_var):
            zero_prefix[idx_var + 1] = zero_prefix[idx_var] + (1 if s[idx_var] == '0' else 0)
            one_prefix[idx_var + 1] = one_prefix[idx_var] + (1 if s[idx_var] == '1' else 0)

        def check_substrings_valid(left_param: int, right_param: int) -> int:
            total_count = 0

            start_var = left_param
            while start_var <= right_param:
                low = start_var
                high = right_param + 1

                while low < high:
                    mid_var = (low + high) // 2

                    zeros_in_range = zero_prefix[mid_var + 1] - zero_prefix[start_var]
                    ones_in_range = one_prefix[mid_var + 1] - one_prefix[start_var]

                    if not (zeros_in_range > k and ones_in_range > k):
                        low = mid_var + 1
                    else:
                        high = mid_var

                max_end = low - 1

                if max_end >= start_var:
                    total_count += max_end - start_var + 1

                start_var += 1

            return total_count

        output_list = []
        for query_index in range(len(queries)):
            l_var, r_var = queries[query_index]
            output_list.append(check_substrings_valid(l_var, r_var))

        return output_list