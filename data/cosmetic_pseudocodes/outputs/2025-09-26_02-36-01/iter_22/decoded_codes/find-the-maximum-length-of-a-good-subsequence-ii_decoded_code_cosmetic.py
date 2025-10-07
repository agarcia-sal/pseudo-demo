from collections import defaultdict

class Solution:
    def maximumLength(self, nums, k):
        totalCount = len(nums)
        matrix = [[0] * (k + 1) for _ in range(totalCount)]
        defaultMaps = [defaultdict(int) for _ in range(k + 1)]
        trackers = [[0, 0, 0] for _ in range(k + 1)]  # Each: [num, highest, second_highest]
        resultVal = 0

        outerIndex = 0
        while outerIndex < totalCount:
            currentNum = nums[outerIndex]
            innerCounter = 0
            while innerCounter <= k:
                matrixRow = matrix[outerIndex]
                defaultMap = defaultMaps[innerCounter]
                trackerElements = trackers[innerCounter]

                accessValue = defaultMap[currentNum]
                matrixRow[innerCounter] = accessValue

                if innerCounter > 0:
                    if trackerElements[0] != currentNum:
                        if matrixRow[innerCounter] < trackerElements[1]:
                            matrixRow[innerCounter] = trackerElements[1]
                    else:
                        if matrixRow[innerCounter] < trackerElements[2]:
                            matrixRow[innerCounter] = trackerElements[2]

                matrixRow[innerCounter] += 1
                currentFValue = matrixRow[innerCounter]

                if defaultMap[currentNum] < currentFValue:
                    defaultMap[currentNum] = currentFValue

                if trackerElements[0] != currentNum:
                    if currentFValue >= trackerElements[1]:
                        trackerElements[2] = trackerElements[1]
                        trackerElements[1] = currentFValue
                        trackerElements[0] = currentNum
                    else:
                        if trackerElements[2] < currentFValue:
                            trackerElements[2] = currentFValue
                else:
                    if trackerElements[1] < currentFValue:
                        trackerElements[1] = currentFValue

                if resultVal < currentFValue:
                    resultVal = currentFValue

                innerCounter += 1
            outerIndex += 1

        return resultVal