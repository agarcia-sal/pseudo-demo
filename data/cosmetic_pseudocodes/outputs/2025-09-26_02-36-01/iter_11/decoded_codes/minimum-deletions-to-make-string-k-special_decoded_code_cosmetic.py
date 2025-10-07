class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def computeFreqMap(text, resultMap):
            idx = 0
            while idx < len(text):
                ch = text[idx]
                if ch in resultMap:
                    resultMap[ch] += 1
                else:
                    resultMap[ch] = 1
                idx += 1

        mapAux = {}
        computeFreqMap(word, mapAux)

        def extractSortedValues(mapIn, outList):
            tempArr = []
            for key in mapIn:
                tempArr.append(mapIn[key])
            tempArr.sort()
            idx2 = 0
            while idx2 < len(tempArr):
                outList.append(tempArr[idx2])
                idx2 += 1

        arrFreq = []
        extractSortedValues(mapAux, arrFreq)

        infPos = float('inf')
        minDel = infPos

        def sumRange(startX, endX, listX):
            resultSum = 0
            if startX <= endX:
                iVal = startX
                while iVal <= endX:
                    resultSum += listX[iVal]
                    iVal += 1
            return resultSum

        def sumExcess(startX, endX, listX, limit):
            accum = 0
            iVal = endX
            while iVal >= startX:
                if listX[iVal] > limit:
                    diff = listX[iVal] - limit
                    accum += diff
                iVal -= 1
            return accum

        def minimumRec(currIdx, freqArr, kVal, currMin):
            if currIdx > len(freqArr) - 1:
                return currMin
            else:
                bound = freqArr[currIdx] + kVal

                deletionsLocal = 0
                deletionsLocal += sumExcess(currIdx + 1, len(freqArr) - 1, freqArr, bound)
                deletionsLocal += sumRange(0, currIdx - 1, freqArr)

                newMin = currMin
                if deletionsLocal < currMin:
                    newMin = deletionsLocal

                return minimumRec(currIdx + 1, freqArr, kVal, newMin)

        resultFinal = minimumRec(0, arrFreq, k, minDel)

        return resultFinal