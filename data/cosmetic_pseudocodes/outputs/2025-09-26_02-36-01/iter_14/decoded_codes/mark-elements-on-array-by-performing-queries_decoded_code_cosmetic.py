import heapq
from typing import List, Tuple

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[int]:
        def extractMin(heapParam):
            return heapq.heappop(heapParam)

        heapContainer = []
        enumerIndex = 0
        while enumerIndex < len(nums):
            iteratorValue = nums[enumerIndex]
            iteratorIndex = enumerIndex
            heapContainer.append([iteratorValue, iteratorIndex])
            enumerIndex += 1
        heapq.heapify(heapContainer)

        collectedMarks = set()
        aggregateSum = 0
        idxCounter = 0
        while idxCounter < len(nums):
            aggregateSum += nums[idxCounter]
            idxCounter += 1

        outputList = []
        queryCursor = 0
        while queryCursor < len(queries):
            currentIndex, currentK = queries[queryCursor]

            if currentIndex not in collectedMarks:
                collectedMarks.add(currentIndex)
                aggregateSum -= nums[currentIndex]

            hitsCounter = 0
            while hitsCounter < currentK and len(heapContainer) > 0:
                valExtracted, idxExtracted = extractMin(heapContainer)
                if idxExtracted not in collectedMarks:
                    collectedMarks.add(idxExtracted)
                    aggregateSum -= valExtracted
                    hitsCounter += 1

            outputList.append(aggregateSum)
            queryCursor += 1

        return outputList