from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        def binsearch(arr: List[int], target: int) -> int:
            left_bound = 0
            right_bound = len(arr)
            while left_bound < right_bound:
                mid_point = (left_bound + right_bound) // 2
                if arr[mid_point] <= target:
                    left_bound = mid_point + 1
                else:
                    right_bound = mid_point
            return left_bound

        alpha = 0
        for zeta in nums:
            if zeta > alpha:
                alpha = zeta

        def count_elements(collection: List[int]) -> dict:
            map_structure = {}
            def add_element(key: int):
                map_structure[key] = map_structure.get(key, 0) + 1
            for element in collection:
                add_element(element)
            return map_structure

        omega = count_elements(nums)
        gamma = [0] * (alpha + 1)

        def proc_i(i: int):
            nu = 0
            def proc_j(j: int):
                nonlocal nu
                nu += omega.get(j, 0)
                if j < len(gamma):
                    gamma[i] -= gamma[j]
            index_j = i
            while index_j <= alpha:
                proc_j(index_j)
                index_j += i
            gamma[i] += nu * (nu - 1) // 2

        index_i = alpha
        while index_i >= 1:
            proc_i(index_i)
            index_i -= 1

        accumulator = [0] * len(gamma)
        acc_sum = 0
        for idx in range(len(gamma)):
            acc_sum += gamma[idx]
            accumulator[idx] = acc_sum

        output_list = []
        def process_query(q_val: int):
            pos = binsearch(accumulator, q_val)
            output_list.append(pos)

        for query_value in queries:
            process_query(query_value)

        return output_list