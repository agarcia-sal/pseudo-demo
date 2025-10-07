from heapq import heapify, heappop
from typing import List

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heapContent = []
        numCounter = 0
        while numCounter < len(nums):
            element = nums[numCounter]
            heapContent.append([element, numCounter])
            numCounter += 1
        heapify(heapContent)

        flaggedSet = set()
        aggregate = 0
        resultList = []
        i = 0
        while i < len(nums):
            aggregate += nums[i]
            i += 1

        queryIdx = 0
        while queryIdx < len(queries):
            currentIndex = queries[queryIdx][0]
            currentK = queries[queryIdx][1]

            if currentIndex not in flaggedSet:
                flaggedSet.add(currentIndex)
                aggregate -= nums[currentIndex]

            removedCount = 0
            while removedCount < currentK and heapContent:
                topEntry = heappop(heapContent)
                val, idxEntry = topEntry[0], topEntry[1]

                if idxEntry not in flaggedSet:
                    flaggedSet.add(idxEntry)
                    aggregate -= val
                    removedCount += 1

            resultList.append(aggregate)
            queryIdx += 1

        return resultList