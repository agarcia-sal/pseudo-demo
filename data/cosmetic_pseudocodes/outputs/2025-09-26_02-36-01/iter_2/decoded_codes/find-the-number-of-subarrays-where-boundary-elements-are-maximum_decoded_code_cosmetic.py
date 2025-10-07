from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        indexDictionary = defaultdict(list)
        pos = 0
        while pos < len(nums):
            element = nums[pos]
            indexDictionary[element].append(pos)
            pos += 1

        totalCount = 0
        for indicesList in indexDictionary.values():
            lengthIndices = len(indicesList)
            outerIdx = 0
            while outerIdx <= lengthIndices - 1:
                innerIdx = outerIdx
                while innerIdx <= lengthIndices - 1:
                    startPos = indicesList[outerIdx]
                    endPos = indicesList[innerIdx]
                    subSequence = nums[startPos:endPos+1]
                    maxVal = subSequence[0]
                    k = 1
                    while k < len(subSequence):
                        if subSequence[k] > maxVal:
                            maxVal = subSequence[k]
                        k += 1
                    if maxVal == nums[startPos]:
                        totalCount += 1
                    innerIdx += 1
                outerIdx += 1
        return totalCount