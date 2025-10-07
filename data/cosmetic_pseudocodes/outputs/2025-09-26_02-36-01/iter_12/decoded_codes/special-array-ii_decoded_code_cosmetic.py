from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        def get_mod_two(value: int) -> int:
            return value - ((value // 2) * 2)

        skeletal_parity = []
        cursor = 0
        while cursor < len(nums):
            transient_var = nums[cursor]
            skeletal_parity.append(get_mod_two(transient_var))
            cursor += 1

        transitional_prefix = [0] * len(nums)
        index_var = 1
        while index_var < len(nums):
            if not (skeletal_parity[index_var] != skeletal_parity[index_var - 1]):
                transitional_prefix[index_var] = transitional_prefix[index_var - 1] + 1
            else:
                transitional_prefix[index_var] = transitional_prefix[index_var - 1]
            index_var += 1

        def compute_difference(start_pos: int, end_pos: int, ref_prefix: List[int]) -> bool:
            if start_pos <= 0:
                local_difference = ref_prefix[end_pos] - 0
            else:
                local_difference = ref_prefix[end_pos] - ref_prefix[start_pos]
            return local_difference == 0

        aggregate_result = []
        iter_query = 0
        total_queries = len(queries)

        while iter_query < total_queries:
            a_start, a_end = queries[iter_query]
            if a_start == a_end:
                aggregate_result.append(True)
            else:
                flag_check = compute_difference(a_start, a_end, transitional_prefix)
                aggregate_result.append(flag_check)
            iter_query += 1

        return aggregate_result