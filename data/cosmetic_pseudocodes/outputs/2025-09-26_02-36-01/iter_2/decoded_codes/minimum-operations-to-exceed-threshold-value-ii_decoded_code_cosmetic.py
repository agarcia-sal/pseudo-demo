import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        operationsCount = 0
        while len(nums) > 1 and nums[0] < k:
            firstElement = heapq.heappop(nums)
            secondElement = heapq.heappop(nums)
            smallerVal = min(firstElement, secondElement)
            largerVal = max(firstElement, secondElement)
            combined = (smallerVal * 2) + largerVal
            heapq.heappush(nums, combined)
            operationsCount += 1
        return operationsCount