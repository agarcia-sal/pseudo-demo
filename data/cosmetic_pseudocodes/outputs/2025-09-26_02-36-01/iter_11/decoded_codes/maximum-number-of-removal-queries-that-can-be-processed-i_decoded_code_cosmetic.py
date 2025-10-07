from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:

        def process_queries(subseq: List[int], queries: List[int]) -> int:
            alpha = 0
            beta = 0
            n, m = len(subseq), len(queries)
            while True:
                if beta == n:
                    break
                if subseq[beta] >= queries[alpha]:
                    beta += 1
                alpha += 1
                if alpha == m:
                    break
            return beta

        omega = len(nums)
        psi = len(queries)
        delta = process_queries(nums, queries)

        def reverse_list(input_list: List[int]) -> List[int]:
            reversed_list = []
            index_var = len(input_list) - 1
            while index_var >= 0:
                reversed_list.append(input_list[index_var])
                index_var -= 1
            return reversed_list

        def concatenate_lists(a: List[int], b: List[int]) -> List[int]:
            result = []
            for element in a:
                result.append(element)
            for element in b:
                result.append(element)
            return result

        def sort_asc(arr: List[int]) -> None:
            if len(arr) <= 1:
                return
            pivot = arr[0]
            left_part = []
            right_part = []
            for it in range(1, len(arr)):
                if arr[it] <= pivot:
                    left_part.append(arr[it])
                else:
                    right_part.append(arr[it])
            sort_asc(left_part)
            sort_asc(right_part)
            idx_merge = 0
            for el in left_part:
                arr[idx_merge] = el
                idx_merge += 1
            arr[idx_merge] = pivot
            idx_merge += 1
            for el in right_part:
                arr[idx_merge] = el
                idx_merge += 1

        for epsilon in range(omega):
            segment_one = []
            idx_inner = 0
            while idx_inner < epsilon:
                segment_one.append(nums[idx_inner])
                idx_inner += 1
            idx_inner = epsilon
            reversed_suffix = []
            while idx_inner < omega:
                idx_inner += 1
            idx_inner = omega - 1
            while idx_inner >= epsilon:
                reversed_suffix.append(nums[idx_inner])
                idx_inner -= 1
            segment_two = reversed_suffix
            combined = concatenate_lists(segment_one, segment_two)

            sort_asc(combined)

            temp_val = process_queries(combined, queries)
            if delta < temp_val:
                delta = temp_val

        return delta