class Solution:
    def maximumLength(self, nums, k):
        def initialize2DArray(rows, cols):
            result = []
            idx1 = 0
            while True:
                if idx1 >= rows:
                    break
                tempRow = []
                idx2 = 0
                while True:
                    if idx2 >= cols:
                        break
                    tempRow.append(0)
                    idx2 += 1
                result.append(tempRow)
                idx1 += 1
            return result

        def createListOfDictionaries(length):
            output = []
            counter = 0
            while True:
                if counter >= length:
                    break
                output.append({})
                counter += 1
            return output

        def maxValue(a, b):
            return a if a > b else b

        totalCount = len(nums)
        limit = k + 1

        matrixF = initialize2DArray(totalCount, limit)
        mapMp = createListOfDictionaries(limit)
        matrixG = initialize2DArray(limit, 3)

        maxAnswer = 0

        outerIndex = 0
        while True:
            if outerIndex >= totalCount:
                break
            currentElem = nums[outerIndex]

            innerIndex = 0
            while True:
                if innerIndex >= limit:
                    break

                dictAtInner = mapMp[innerIndex]
                if currentElem in dictAtInner:
                    matrixF[outerIndex][innerIndex] = dictAtInner[currentElem]
                else:
                    matrixF[outerIndex][innerIndex] = 0

                if innerIndex > 0:
                    prevGFirst = matrixG[innerIndex - 1][0]
                    prevGSecond = matrixG[innerIndex - 1][1]
                    prevGThird = matrixG[innerIndex - 1][2]

                    if prevGFirst != currentElem:
                        matrixF[outerIndex][innerIndex] = maxValue(matrixF[outerIndex][innerIndex], prevGSecond)
                    else:
                        matrixF[outerIndex][innerIndex] = maxValue(matrixF[outerIndex][innerIndex], prevGThird)

                matrixF[outerIndex][innerIndex] += 1

                if currentElem in mapMp[innerIndex]:
                    mapMp[innerIndex][currentElem] = maxValue(mapMp[innerIndex][currentElem], matrixF[outerIndex][innerIndex])
                else:
                    mapMp[innerIndex][currentElem] = matrixF[outerIndex][innerIndex]

                gFirst = matrixG[innerIndex][0]
                gSecond = matrixG[innerIndex][1]
                gThird = matrixG[innerIndex][2]
                curFVal = matrixF[outerIndex][innerIndex]

                if gFirst != currentElem:
                    if curFVal >= gSecond:
                        matrixG[innerIndex][2] = gSecond
                        matrixG[innerIndex][1] = curFVal
                        matrixG[innerIndex][0] = currentElem
                    else:
                        matrixG[innerIndex][2] = maxValue(gThird, curFVal)
                else:
                    matrixG[innerIndex][1] = maxValue(gSecond, curFVal)

                maxAnswer = maxValue(maxAnswer, curFVal)

                innerIndex += 1

            outerIndex += 1

        return maxAnswer