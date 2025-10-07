from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def compute_parity(index: int, parity_accum: List[int]) -> List[int]:
            if index >= len(nums):
                return parity_accum
            remainder_aux = nums[index] % 2
            return compute_parity(index + 1, parity_accum + [remainder_aux])

        def form_prefix_special(current_idx: int, prefix_list: List[int]) -> List[int]:
            if current_idx >= len(nums):
                return prefix_list
            prev_parity = parity[current_idx - 1]
            curr_parity = parity[current_idx]
            prev_prefix = prefix_list[current_idx - 1]

            if curr_parity == prev_parity:
                prefix_elem = prev_prefix + 1
            else:
                prefix_elem = prev_prefix

            updated_prefix = prefix_list[:current_idx] + [prefix_elem] + prefix_list[current_idx + 1:]
            return form_prefix_special(current_idx + 1, updated_prefix)

        def process_queries(q_idx: int, res_accum: List[bool]) -> List[bool]:
            if q_idx >= len(queries):
                return res_accum
            start_idx, end_idx = queries[q_idx]

            if start_idx == end_idx:
                append_val = True
            else:
                left_cond = 0
                if start_idx > 0:
                    left_cond = prefix_special[start_idx]
                diff_val = prefix_special[end_idx] - left_cond
                append_val = (diff_val == 0)

            return process_queries(q_idx + 1, res_accum + [append_val])

        parity = compute_parity(0, [])
        prefix_special = [0 for _ in range(len(nums))]
        prefix_special = form_prefix_special(1, prefix_special)
        result = process_queries(0, [])
        return result