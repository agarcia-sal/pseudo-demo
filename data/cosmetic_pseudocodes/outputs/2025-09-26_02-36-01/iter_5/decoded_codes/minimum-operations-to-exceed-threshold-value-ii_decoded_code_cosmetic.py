import heapq
from typing import List

class Solution:
    def minOperations(self, k: int, nums: List[int]) -> int:
        heapq.heapify(nums)

        countOps = 0

        def combineHeap(heapRef) -> None:
            nonlocal countOps
            if not (heapRef[0] < k and len(heapRef) > 1):
                return
            firstElem = heapq.heappop(heapRef)
            secondElem = heapq.heappop(heapRef)
            smallerVal = firstElem if firstElem < secondElem else secondElem
            biggerVal = firstElem if firstElem > secondElem else secondElem
            combined = (smallerVal + smallerVal) + biggerVal
            heapq.heappush(heapRef, combined)
            countOps += 1
            combineHeap(heapRef)

        combineHeap(nums)
        return countOps