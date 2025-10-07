from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0
            beta = 0
            len_subseq = len(subseq)
            len_queries = len(queries)
            while beta < len_queries and alpha < len_subseq:
                if subseq[alpha] >= queries[beta]:
                    alpha += 1
                beta += 1
            return alpha

        def extract_subsequence(src: List[int], start_index: int, end_index: int) -> List[int]:
            return src[start_index:end_index]

        def reverse_list(lst: List[int]) -> List[int]:
            return lst[::-1]

        def sort_ascending(arr: List[int]) -> List[int]:
            # Implemented bubble sort as in pseudocode but optimized with early break
            n = len(arr)
            arr_copy = arr[:]  # copy to avoid mutating input
            while True:
                swapped = False
                for i in range(1, n):
                    if arr_copy[i - 1] > arr_copy[i]:
                        arr_copy[i - 1], arr_copy[i] = arr_copy[i], arr_copy[i - 1]
                        swapped = True
                if not swapped:
                    break
                n -= 1
            return arr_copy

        achieved = process_queries(nums, queries)

        for epsilon in range(len(nums)):
            part_a = extract_subsequence(nums, 0, epsilon)
            part_b = extract_subsequence(nums, epsilon, len(nums))
            part_b_rev = reverse_list(part_b)
            combined_seq = part_a + part_b_rev
            sorted_seq = sort_ascending(combined_seq)
            candidate = process_queries(sorted_seq, queries)
            if candidate > achieved:
                achieved = candidate

        return achieved