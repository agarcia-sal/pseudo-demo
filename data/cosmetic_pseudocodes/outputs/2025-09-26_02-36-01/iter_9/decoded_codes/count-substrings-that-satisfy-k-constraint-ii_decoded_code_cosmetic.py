from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        q = len(s)
        arr_zero_counts = [0] * (q + 1)
        arr_one_counts = [0] * (q + 1)

        def compute_prefixes():
            for idx in range(q):
                arr_zero_counts[idx + 1] = arr_zero_counts[idx] + (1 if s[idx] == '0' else 0)
                arr_one_counts[idx + 1] = arr_one_counts[idx] + (1 if s[idx] == '1' else 0)

        def compute_valid_substrings(x: int, y: int) -> int:
            total_valid = 0

            def process_start(pos: int):
                nonlocal total_valid
                if pos > y:
                    return
                low, high = pos, y + 1
                while True:
                    mid_val = (low + high) // 2
                    zero_subcount = arr_zero_counts[mid_val + 1] - arr_zero_counts[pos]
                    one_subcount = arr_one_counts[mid_val + 1] - arr_one_counts[pos]
                    if zero_subcount <= k or one_subcount <= k:
                        low = mid_val + 1
                    else:
                        high = mid_val
                    if low >= high:
                        break
                furthest_end = low - 1
                if furthest_end >= pos:
                    total_valid += (furthest_end - pos + 1)

            ptr = x
            while ptr <= y:
                process_start(ptr)
                ptr += 1
            return total_valid

        compute_prefixes()
        answer_list = []

        def collect_results():
            idx_query = 0
            while idx_query < len(queries):
                left_bound, right_bound = queries[idx_query]
                answer_list.append(compute_valid_substrings(left_bound, right_bound))
                idx_query += 1

        collect_results()
        return answer_list