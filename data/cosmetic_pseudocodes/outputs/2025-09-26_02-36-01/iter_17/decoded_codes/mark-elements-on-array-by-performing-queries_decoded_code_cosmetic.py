import heapq
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        priority_queue = []
        already_flagged = set()
        acc_sum = sum(nums)
        answers = []
        p = 0
        q = 0

        while p < len(nums):
            priority_queue.append((nums[p], p))
            p += 1

        heapq.heapify(priority_queue)

        while q < len(queries):
            idx_query, k_query = queries[q]

            if idx_query not in already_flagged:
                already_flagged.add(idx_query)
                acc_sum -= nums[idx_query]

            current_count = 0
            while current_count < k_query and priority_queue:
                extracted_val, extracted_idx = heapq.heappop(priority_queue)
                if extracted_idx not in already_flagged:
                    already_flagged.add(extracted_idx)
                    acc_sum -= extracted_val
                    current_count += 1

            answers.append(acc_sum)
            q += 1

        return answers