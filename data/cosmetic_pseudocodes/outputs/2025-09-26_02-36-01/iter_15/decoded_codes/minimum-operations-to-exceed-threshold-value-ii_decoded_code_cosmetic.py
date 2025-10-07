import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = nums[:]
        heapq.heapify(q)
        c = 0
        while True:
            if not (q[0] < k and len(q) > 1):
                break
            a = heapq.heappop(q)
            b = heapq.heappop(q)
            m = (min(a, b) * 2) + max(a, b)
            heapq.heappush(q, m)
            c += 1
        return c