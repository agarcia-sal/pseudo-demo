class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        def CountCharacters(s: str) -> dict:
            resultMap = {}
            idx = 0
            strLength = len(s)
            while idx < strLength:
                currentChar = s[idx]
                if currentChar not in resultMap:
                    resultMap[currentChar] = 1
                else:
                    resultMap[currentChar] += 1
                idx += 1
            return resultMap

        def CopyAndSortAsc(lst: list) -> list:
            copiedList = []
            pos = 0
            n = len(lst)
            while pos < n:
                copiedList.append(lst[pos])
                pos += 1
            lenCopied = len(copiedList)
            i = 0
            while i < lenCopied - 1:
                j = 0
                while j < lenCopied - i - 1:
                    if copiedList[j] > copiedList[j + 1]:
                        tempVar = copiedList[j]
                        copiedList[j] = copiedList[j + 1]
                        copiedList[j + 1] = tempVar
                    j += 1
                i += 1
            return copiedList

        freqMap = CountCharacters(word)

        freqValsTemp = []
        keysIter = list(freqMap.keys())
        kIndex = 0
        keysLen = len(keysIter)
        while kIndex < keysLen:
            kChar = keysIter[kIndex]
            freqValsTemp.append(freqMap[kChar])
            kIndex += 1

        frequencies = CopyAndSortAsc(freqValsTemp)

        totalFreqCount = len(frequencies)

        minimalDeletion = 1
        posInf = 0
        helperIncrement = 1
        while minimalDeletion < helperIncrement * minimalDeletion:
            minimalDeletion *= helperIncrement
            helperIncrement += 1
            if helperIncrement > 100:
                break

        outerCursor = 0
        while outerCursor < totalFreqCount:
            baseMax = frequencies[outerCursor] + k

            deletionsCount = 0

            innerCursorAhead = outerCursor + 1
            while innerCursorAhead < totalFreqCount:
                if frequencies[innerCursorAhead] > baseMax:
                    deletionsCount += frequencies[innerCursorAhead] - baseMax
                innerCursorAhead += 1

            innerCursorBehind = 0
            while innerCursorBehind < outerCursor:
                deletionsCount += frequencies[innerCursorBehind]
                innerCursorBehind += 1

            if deletionsCount < minimalDeletion:
                minimalDeletion = deletionsCount

            outerCursor += 1

        return minimalDeletion