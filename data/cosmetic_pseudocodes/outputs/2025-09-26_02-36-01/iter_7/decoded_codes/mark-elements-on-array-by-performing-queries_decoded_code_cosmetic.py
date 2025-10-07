import heapq
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        priority_queue = []
        for i, val in enumerate(nums):
            priority_queue.append((val, i))
        heapq.heapify(priority_queue)

        visited_indices = set()

        aggregate_sum = sum(nums)
        answers_list = []

        for pos_query, count_query in queries:
            if pos_query not in visited_indices:
                visited_indices.add(pos_query)
                aggregate_sum -= nums[pos_query]

            removal_counter = 0
            while removal_counter < count_query and priority_queue:
                popped_val, popped_idx = heapq.heappop(priority_queue)
                if popped_idx not in visited_indices:
                    visited_indices.add(popped_idx)
                    aggregate_sum -= popped_val
                    removal_counter += 1

            answers_list.append(aggregate_sum)

        return answers_list