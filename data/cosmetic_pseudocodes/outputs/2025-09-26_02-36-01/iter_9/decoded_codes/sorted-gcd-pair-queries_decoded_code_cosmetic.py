from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # Convert 1-based indexing pseudocode to 0-based indexing Python

        def max_element(arr: List[int]) -> int:
            idx = 0
            cur = arr[0]
            k = 1
            n = len(arr)
            while k < n:
                if arr[k] > cur:
                    cur = arr[k]
                    idx = k
                k += 1
            return cur

        def count_elements(arr: List[int]) -> dict:
            dict_cnt = {}
            pos = 0
            n = len(arr)
            while pos < n:
                key = arr[pos]
                dict_cnt[key] = dict_cnt.get(key, 0) + 1
                pos += 1
            return dict_cnt

        def bisect_right(arr: List[int], x: int) -> int:
            # Python's bisect_right is 0-based, but pseudocode returns 1-based index
            # So we need to add 1 to the result to align.
            return bisect.bisect_right(arr, x) + 1

        maxVal = max_element(nums)
        counts = count_elements(nums)
        array_g = [0] * (maxVal + 1)

        # The decrement_range function is defined but never called in the pseudocode,
        # so we omit it in final implementation to preserve functionality.

        i_var = maxVal
        while i_var >= 1:
            value_accum = 0

            def inner_loop(j_var: int, max_j: int):
                nonlocal value_accum
                if j_var > max_j:
                    return
                if j_var in counts:
                    value_accum += counts[j_var]
                array_g[i_var] -= array_g[j_var]
                inner_loop(j_var + i_var, max_j)

            inner_loop(i_var, maxVal)
            value_accum_combinations = value_accum * (value_accum - 1) // 2
            array_g[i_var] += value_accum_combinations
            i_var -= 1

        def accumulate(arr: List[int]) -> List[int]:
            n = len(arr)
            result_arr = [0] * n
            result_arr[0] = arr[0]
            z_idx = 1
            while z_idx < n:
                result_arr[z_idx] = result_arr[z_idx - 1] + arr[z_idx]
                z_idx += 1
            return result_arr

        pref_sum = accumulate(array_g)
        output_list = []

        def process_queries(idx: int):
            if idx >= len(queries):
                return
            q_val = queries[idx]
            pos_ins = bisect_right(pref_sum, q_val)
            output_list.append(pos_ins)
            process_queries(idx + 1)

        process_queries(0)

        return output_list