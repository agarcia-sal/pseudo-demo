from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries_p: List[int]) -> int:
            def recur_process(index_p: int, queries_p: List[int]) -> int:
                if index_p == len(subseq):
                    return index_p
                elif not queries_p:
                    return index_p
                else:
                    if subseq[index_p] >= queries_p[0]:
                        return recur_process(index_p + 1, queries_p[1:])
                    else:
                        return recur_process(index_p, queries_p[1:])
            return recur_process(0, queries_p)

        total_nums = len(nums)
        total_queries = len(queries)

        result_max = process_queries(nums, queries)

        def iterate_indices(current_idx: int, acc_max: int) -> int:
            if current_idx == total_nums:
                return acc_max
            else:
                prefix_slice = nums[0:current_idx] if current_idx > 0 else []

                suffix_slice = nums[current_idx:total_nums]

                def reverse_list(lst: List[int]) -> List[int]:
                    def rev_rec(i: int, acc: List[int]) -> List[int]:
                        if i < 0:
                            return acc
                        else:
                            return rev_rec(i - 1, acc + [lst[i]])
                    return rev_rec(len(lst) - 1, [])

                reversed_suffix = reverse_list(suffix_slice)

                def concat_lists(a: List[int], b: List[int]) -> List[int]:
                    def concat_rec(i: int, res: List[int]) -> List[int]:
                        if i == len(a):
                            return res + b
                        else:
                            return concat_rec(i + 1, res + [a[i]])
                    return concat_rec(0, [])

                combined = concat_lists(prefix_slice, reversed_suffix)

                def selection_sort(arr: List[int]) -> List[int]:
                    def find_min_index(lst: List[int], start: int) -> int:
                        if start == len(lst) - 1:
                            return start
                        else:
                            rest_min_idx = find_min_index(lst, start + 1)
                            if lst[start] < lst[rest_min_idx]:
                                return start
                            else:
                                return rest_min_idx

                    def sort_rec(lst: List[int], idx: int) -> List[int]:
                        if idx == len(lst):
                            return lst
                        else:
                            min_idx = find_min_index(lst, idx)
                            lst2 = lst[:]
                            lst2[idx], lst2[min_idx] = lst2[min_idx], lst2[idx]
                            return sort_rec(lst2, idx + 1)

                    return sort_rec(arr, 0)

                sorted_combined = selection_sort(combined)

                candidate = process_queries(sorted_combined, queries)
                new_max = acc_max
                if candidate > new_max:
                    new_max = candidate
                return iterate_indices(current_idx + 1, new_max)

        final_answer = iterate_indices(0, result_max)
        return final_answer