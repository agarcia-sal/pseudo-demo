import heapq
from typing import List, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        min_heap = [(value, index) for index, value in enumerate(nums)]
        heapq.heapify(min_heap)

        marked_indices = set()
        total_sum = sum(nums)
        result = []

        for index_i, k_i in queries:
            if index_i not in marked_indices:
                marked_indices.add(index_i)
                total_sum -= nums[index_i]

            count = 0
            while count < k_i and min_heap:
                value, index = heapq.heappop(min_heap)
                if index not in marked_indices:
                    marked_indices.add(index)
                    total_sum -= value
                    count += 1

            result.append(total_sum)

        return result