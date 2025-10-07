import heapq
from typing import List, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        temp_heap = [(nums[p], p) for p in range(len(nums))]
        heapq.heapify(temp_heap)

        visited = set()
        aggregate = sum(nums)
        output_list = []

        for current_j, current_l in queries:
            if current_j not in visited:
                visited.add(current_j)
                aggregate -= nums[current_j]

            x = 0
            while x < current_l and temp_heap:
                val, idx = heapq.heappop(temp_heap)
                if idx in visited:
                    continue
                visited.add(idx)
                aggregate -= val
                x += 1

            output_list.append(aggregate)

        return output_list