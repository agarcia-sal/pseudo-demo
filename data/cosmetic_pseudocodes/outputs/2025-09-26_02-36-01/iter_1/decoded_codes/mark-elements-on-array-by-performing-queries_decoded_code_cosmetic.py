import heapq
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        priority_queue = [[num, idx] for idx, num in enumerate(nums)]
        heapq.heapify(priority_queue)

        flagged = set()
        running_total = sum(nums)
        outputs = []

        for current_index, remove_count in queries:
            if current_index not in flagged:
                flagged.add(current_index)
                running_total -= nums[current_index]

            removed_items = 0
            while removed_items < remove_count and priority_queue:
                val, pos = heapq.heappop(priority_queue)
                if pos not in flagged:
                    flagged.add(pos)
                    running_total -= val
                    removed_items += 1

            outputs.append(running_total)

        return outputs