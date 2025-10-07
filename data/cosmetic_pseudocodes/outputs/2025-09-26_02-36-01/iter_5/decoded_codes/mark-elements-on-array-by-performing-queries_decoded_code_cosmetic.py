import heapq
from typing import List, Set, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def recursivePop(heapRef: List[Tuple[int, int]], marksRef: Set[int], kVal: int, counterVal: int, sumRef: int) -> Tuple[int, int]:
            if counterVal >= kVal or not heapRef:
                return sumRef, counterVal
            valTmp, idxTmp = heapq.heappop(heapRef)
            if idxTmp not in marksRef:
                marksRef.add(idxTmp)
                sumRef -= valTmp
                counterVal += 1
            return recursivePop(heapRef, marksRef, kVal, counterVal, sumRef)

        heapContainer = []
        position = 0
        length = len(nums)
        while position < length:
            currentVal = nums[position]
            pairEntry = (currentVal, position)
            heapContainer.append(pairEntry)
            position += 1

        heapq.heapify(heapContainer)
        markedSet = set()
        aggregateSum = 0
        idxCounter = 0
        while idxCounter < length:
            aggregateSum += nums[idxCounter]
            idxCounter += 1
        outputList = []

        queryIdx = 0
        queriesLength = len(queries)
        while queryIdx < queriesLength:
            queryPair = queries[queryIdx]
            qIndex, qK = queryPair[0], queryPair[1]

            if qIndex not in markedSet:
                markedSet.add(qIndex)
                aggregateSum -= nums[qIndex]

            poppedCount = 0
            aggregateSum, poppedCount = recursivePop(heapContainer, markedSet, qK, poppedCount, aggregateSum)

            outputList.append(aggregateSum)
            queryIdx += 1

        return outputList