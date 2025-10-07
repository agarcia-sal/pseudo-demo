from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            def recur_process(idx: int, itr: int) -> int:
                if itr >= len(queries):
                    return idx
                if idx >= len(subseq):
                    return idx
                if subseq[idx] >= queries[itr]:
                    return recur_process(idx + 1, itr + 1)
                else:
                    return recur_process(idx, itr + 1)
            return recur_process(0, 0)

        length_nums = len(nums)
        length_queries = len(queries)
        max_proc = process_queries(nums, queries)

        def iterate_indices(idx: int) -> None:
            if idx >= length_nums:
                return
            comp_var = idx - 1
            temp_list_p = nums[:comp_var+1] if comp_var >= 0 else []
            temp_list_s = nums[idx:]
            rev_suf = temp_list_s[::-1]

            combined_subseq = temp_list_p + rev_suf

            def sort_asc(list_in: List[int]) -> List[int]:
                def swap_elements(lst: List[int], pos1: int, pos2: int) -> None:
                    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

                length_in = len(list_in)

                def bubble_sort_pass(j: int) -> None:
                    if j < length_in - 1:
                        if list_in[j] > list_in[j + 1]:
                            swap_elements(list_in, j, j + 1)
                        bubble_sort_pass(j + 1)

                def bubble_sort_outer(i: int) -> None:
                    if i < length_in:
                        bubble_sort_pass(0)
                        bubble_sort_outer(i + 1)

                bubble_sort_outer(0)
                return list_in

            sorted_subseq = sort_asc(combined_subseq)

            cand_proc = process_queries(sorted_subseq, queries)
            nonlocal max_proc
            if cand_proc > max_proc:
                max_proc = cand_proc

            iterate_indices(idx + 1)

        iterate_indices(0)
        return max_proc