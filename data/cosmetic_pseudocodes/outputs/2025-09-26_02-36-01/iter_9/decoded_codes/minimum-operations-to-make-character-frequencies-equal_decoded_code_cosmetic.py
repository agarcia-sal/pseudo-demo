class Solution:
    def makeStringGood(self, s: str) -> int:
        def ordinal(ch: str) -> int:
            return ord(ch)

        def createZeroList(length: int) -> list[int]:
            return [0] * length

        alphaCount = createZeroList(26)
        for ch in s:
            charVal = ordinal(ch)
            baseVal = ordinal('a')
            posIndex = charVal - baseVal
            alphaCount[posIndex] += 1

        def _getMinOperations(freqArray: list[int], targetVal: int) -> int:
            dpArr = createZeroList(27)
            currIndex = 25

            while currIndex >= 0:
                deleteAll = freqArray[currIndex]

                if targetVal > freqArray[currIndex]:
                    deleteOrInsert = targetVal - freqArray[currIndex]
                else:
                    deleteOrInsert = freqArray[currIndex] - targetVal

                option1 = min(deleteAll, deleteOrInsert + dpArr[currIndex + 1])

                if (currIndex + 1) < 26 and freqArray[currIndex + 1] < targetVal:
                    nextDeficit = targetVal - freqArray[currIndex + 1]

                    if freqArray[currIndex] <= targetVal:
                        needToChange = freqArray[currIndex]
                    else:
                        needToChange = freqArray[currIndex] - targetVal

                    if nextDeficit > needToChange:
                        combinedChange = needToChange + (nextDeficit - needToChange)
                    else:
                        combinedChange = nextDeficit + (needToChange - nextDeficit)

                    option2 = min(option1, combinedChange + dpArr[currIndex + 2])
                else:
                    option2 = option1

                dpArr[currIndex] = option2
                currIndex -= 1

            return dpArr[0]

        maxFreq = max(alphaCount) if alphaCount else 0

        searchVal = 1
        resultVal = None
        firstTime = True
        while searchVal <= maxFreq:
            tempRes = _getMinOperations(alphaCount, searchVal)
            if firstTime:
                resultVal = tempRes
                firstTime = False
            elif tempRes < resultVal:
                resultVal = tempRes
            searchVal += 1

        return resultVal if resultVal is not None else 0