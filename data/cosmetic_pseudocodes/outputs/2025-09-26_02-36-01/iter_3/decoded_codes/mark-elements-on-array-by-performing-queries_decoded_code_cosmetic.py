import heapq
from typing import List, Set

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        priority_queue = []
        for pos, val in enumerate(nums):
            priority_queue.append([val, pos])
        heapq.heapify(priority_queue)

        flagged_positions: Set[int] = set()
        aggregate_total = sum(nums)

        output_list = []
        for query in queries:
            query_pos, threshold_k = query

            if query_pos not in flagged_positions:
                flagged_positions.add(query_pos)
                aggregate_total -= nums[query_pos]

            removals_remaining = threshold_k
            while removals_remaining > 0 and priority_queue:
                val, pos = heapq.heappop(priority_queue)

                if pos not in flagged_positions:
                    flagged_positions.add(pos)
                    aggregate_total -= val
                    removals_remaining -= 1

            output_list.append(aggregate_total)

        return output_list