from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums):
        mapIndices = defaultdict(list)

        posCounter = 0
        while posCounter < len(nums):
            mapIndices[nums[posCounter]].append(posCounter)
            posCounter += 1

        totalCount = 0
        for keyVal in mapIndices.keys():
            idxList = mapIndices[keyVal]
            lenIdx = len(idxList)

            outerIdx = 0
            while True:
                if outerIdx >= lenIdx:
                    break

                innerIdx = outerIdx
                while True:
                    if innerIdx >= lenIdx:
                        break

                    startPos = idxList[outerIdx]
                    endPos = idxList[innerIdx]

                    subArray = nums[startPos:endPos+1]

                    maxVal = subArray[0]
                    subIdx = 1
                    while subIdx < len(subArray):
                        if subArray[subIdx] > maxVal:
                            maxVal = subArray[subIdx]
                        subIdx += 1

                    if maxVal == nums[startPos]:
                        totalCount += 1

                    innerIdx += 1

                outerIdx += 1

        return totalCount