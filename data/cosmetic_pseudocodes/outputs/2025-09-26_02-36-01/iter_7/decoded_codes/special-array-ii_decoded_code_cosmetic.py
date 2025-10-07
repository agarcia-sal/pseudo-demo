from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        ZERO_CONST = 0
        ONE_CONST = ZERO_CONST + 1
        TWO_CONST = ONE_CONST + ONE_CONST

        parity_flags = []
        index_counter = ZERO_CONST
        length_nums = len(nums)
        while index_counter < length_nums:
            current_num = nums[index_counter]
            mod_result = current_num - TWO_CONST * (current_num // TWO_CONST)
            parity_flags.append(mod_result)
            index_counter += ONE_CONST

        special_prefix = [ZERO_CONST] * length_nums

        idx_iter = ONE_CONST
        while idx_iter < length_nums:
            if not (parity_flags[idx_iter] != parity_flags[idx_iter - ONE_CONST]):
                special_prefix[idx_iter] = special_prefix[idx_iter - ONE_CONST] + ONE_CONST
            else:
                special_prefix[idx_iter] = special_prefix[idx_iter - ONE_CONST]
            idx_iter += ONE_CONST

        output_collection = []
        query_idx = ZERO_CONST
        total_queries = len(queries)
        while query_idx < total_queries:
            current_query = queries[query_idx]
            start_pos = current_query[ZERO_CONST]
            end_pos = current_query[ONE_CONST]

            if (start_pos - end_pos) * (end_pos - start_pos) == ZERO_CONST:
                output_collection.append(True)
            else:
                diff_check = special_prefix[end_pos] - (special_prefix[start_pos - ONE_CONST] if start_pos > ZERO_CONST else ZERO_CONST)
                output_collection.append(diff_check == ZERO_CONST)

            query_idx += ONE_CONST

        return output_collection