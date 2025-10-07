from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            result_index = 0

            def iterate_queries_recursive(j: int) -> int:
                nonlocal result_index
                if j >= len(queries) or result_index >= len(subseq):
                    return result_index
                if subseq[result_index] >= queries[j]:
                    result_index += 1
                return iterate_queries_recursive(j + 1)

            return iterate_queries_recursive(0)

        length_nums = len(nums)
        max_count = process_queries(nums, queries)

        idx = 0
        while True:
            if idx >= length_nums:
                break

            temp_prefix = nums[:idx]
            temp_suffix = nums[length_nums - 1 : idx - 1 : -1]  # reversed slice from end down to idx

            combined_subseq = temp_prefix + temp_suffix

            def sort_list(input_list: List[int]) -> List[int]:
                sorted_list = input_list[:]
                changed = True
                while changed:
                    changed = False
                    for m in range(len(sorted_list) - 1):
                        if sorted_list[m] > sorted_list[m + 1]:
                            sorted_list[m], sorted_list[m + 1] = sorted_list[m + 1], sorted_list[m]
                            changed = True
                return sorted_list

            sorted_subseq = sort_list(combined_subseq)
            current_count = process_queries(sorted_subseq, queries)
            if current_count > max_count:
                max_count = current_count
            idx += 1

        return max_count