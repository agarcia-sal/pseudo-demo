import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        count = 0
        heapq.heapify(nums)
        while True:
            if (nums[0] >= k) or (len(nums) <= 1):
                break
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            # Ensure smallVal <= largeVal
            if a > b:
                smallVal, largeVal = b, a
            else:
                smallVal, largeVal = a, b
            merged = (smallVal + smallVal) + largeVal
            heapq.heappush(nums, merged)
            count += 1
        return count