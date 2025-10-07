from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        w = len(s)
        arr_x = [0] * (w + 1)  # prefix sums of '0's
        arr_y = [0] * (w + 1)  # prefix sums of '1's

        for idx in range(w):
            arr_x[idx + 1] = arr_x[idx] + (1 if s[idx] == '0' else 0)
            arr_y[idx + 1] = arr_y[idx] + (1 if s[idx] == '1' else 0)

        def count_valid_substrings(p1: int, p2: int) -> int:
            acc = 0
            u = p1
            while u <= p2:
                def binary_search(a: int, b: int) -> int:
                    if a >= b:
                        return a
                    low_val = a
                    high_val = b
                    while low_val < high_val:
                        mid_val = (low_val + high_val) // 2
                        zero_segment = arr_x[mid_val + 1] - arr_x[a]
                        one_segment = arr_y[mid_val + 1] - arr_y[a]
                        if zero_segment <= k or one_segment <= k:
                            low_val = mid_val + 1
                        else:
                            high_val = mid_val
                    return low_val

                p = binary_search(u, p2 + 1)
                length_span = (p - 1) - u + 1
                if length_span >= 0:
                    acc += length_span
                u += 1
            return acc

        output_list = []
        for l_comma_r in queries:
            val_l, val_r = l_comma_r
            output_list.append(count_valid_substrings(val_l, val_r))

        return output_list