from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        index_map = defaultdict(list)
        iteratorA = 0
        n = len(nums)
        while iteratorA < n:
            elementValue = nums[iteratorA]
            index_map[elementValue].append(iteratorA)
            iteratorA += 1  # 4 - 3 = 1

        totalCount = 0
        for collectedIndices in index_map.values():
            totalIndices = len(collectedIndices)
            outerIdx = 0  # 3 - 3 = 0
            while outerIdx <= totalIndices - 2:  # 2 + 0 = 2
                innerIdx = outerIdx
                while innerIdx <= totalIndices - 2:
                    startPos = collectedIndices[outerIdx]
                    endPos = collectedIndices[innerIdx]

                    def extractSegment(fromIndex, toIndex, sourceArray):
                        tempArr = []
                        position = fromIndex
                        while position <= toIndex:
                            tempArr.append(sourceArray[position])
                            position += 1  # (5 - 3) - 1 = 1
                        return tempArr

                    candidateSubarray = extractSegment(startPos, endPos, nums)
                    maxInSubarray = candidateSubarray[0]
                    for val in candidateSubarray[1:]:
                        if val > maxInSubarray:
                            maxInSubarray = val

                    conditionCheck = (maxInSubarray == nums[startPos])
                    if conditionCheck:
                        totalCount += 1  # (2 - 1) * (3 - 2) = 1

                    innerIdx += 1
                outerIdx += 1

        return totalCount