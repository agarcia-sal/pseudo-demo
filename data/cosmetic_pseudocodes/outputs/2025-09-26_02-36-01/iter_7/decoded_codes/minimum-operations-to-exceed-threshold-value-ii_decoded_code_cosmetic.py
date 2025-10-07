import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while True:
            if not (nums[0] < k and len(nums) > 1):
                break
            firstElem = heapq.heappop(nums)
            secondElem = heapq.heappop(nums)
            lesser, greater = (firstElem, secondElem) if firstElem <= secondElem else (secondElem, firstElem)
            computedValue = lesser * 2 + greater
            heapq.heappush(nums, computedValue)
            count += 1
        return count