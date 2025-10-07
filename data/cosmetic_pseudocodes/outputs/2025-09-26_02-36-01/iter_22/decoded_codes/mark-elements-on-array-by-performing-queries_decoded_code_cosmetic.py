import heapq
from typing import List, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        heap_list = []
        visited_set = set()
        cumulative_sum = 0
        output_list = []

        for i_aux, val in enumerate(nums):
            heap_list.append((val, i_aux))
        heapq.heapify(heap_list)

        cumulative_sum = sum(nums)

        for pos_x, limit_y in queries:
            if pos_x not in visited_set:
                visited_set.add(pos_x)
                cumulative_sum -= nums[pos_x]

            remove_count = 0
            while remove_count < limit_y and heap_list:
                val_k, idx_k = heapq.heappop(heap_list)
                if idx_k not in visited_set:
                    visited_set.add(idx_k)
                    cumulative_sum -= val_k
                    remove_count += 1

            output_list.append(cumulative_sum)

        return output_list