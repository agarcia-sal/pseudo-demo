import heapq

class Solution:
    def unmarkedSumArray(self, nums, queries):
        heapList = []
        for iterator, currentValue in enumerate(nums):
            heapList.append((currentValue, iterator))
        heapq.heapify(heapList)

        excludedIndices = set()
        aggregateSum = sum(nums)

        outcome = []
        for query in queries:
            currentIndex, requiredCount = query

            if currentIndex not in excludedIndices:
                excludedIndices.add(currentIndex)
                aggregateSum -= nums[currentIndex]

            tempCount = 0
            while tempCount < requiredCount and heapList:
                valueExtracted, indexExtracted = heapq.heappop(heapList)
                if indexExtracted not in excludedIndices:
                    excludedIndices.add(indexExtracted)
                    aggregateSum -= valueExtracted
                    tempCount += 1

            outcome.append(aggregateSum)

        return outcome