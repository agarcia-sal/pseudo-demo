from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        def addIndexToMap(key, container, index):
            if key not in container:
                container[key] = []
            container[key].append(index)

        index_map = {}
        currentIndex = 0

        while currentIndex < len(nums):
            addIndexToMap(nums[currentIndex], index_map, currentIndex)
            currentIndex += 1

        totalCount = 0
        for collectedIndices in index_map.values():
            lengthIndices = len(collectedIndices)
            outerInd = 0

            while outerInd <= lengthIndices - 1:
                innerInd = outerInd
                while innerInd <= lengthIndices - 1:
                    startIndex = collectedIndices[outerInd]
                    endIndex = collectedIndices[innerInd]

                    currentRange = []
                    scanPos = startIndex
                    while scanPos <= endIndex:
                        currentRange.append(nums[scanPos])
                        scanPos += 1

                    maxElement = nums[startIndex]
                    if not (maxElement < max(currentRange)):
                        totalCount += 1

                    innerInd += 1
                outerInd += 1

        return totalCount