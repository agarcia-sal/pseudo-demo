class Solution:
    def minimizeStringValue(self, s: str) -> str:
        def countCharacters(inputStr):
            dictResult = {}
            idxCounter = 0
            lenInput = len(inputStr)
            while idxCounter < lenInput:
                curCh = inputStr[idxCounter]
                if curCh in dictResult:
                    dictResult[curCh] += 1
                else:
                    dictResult[curCh] = 1
                idxCounter += 1
            return dictResult

        freqMap = countCharacters(s)

        def removeEntryIfExists(dictRef, keyVal):
            if keyVal in dictRef:
                del dictRef[keyVal]

        removeEntryIfExists(freqMap, '?')

        def gatherIndices(strIn, targetChar):
            acc = []
            pos = 0
            lenStr = len(strIn)
            while pos < lenStr:
                if strIn[pos] == targetChar:
                    acc.append(pos)
                pos += 1
            return acc

        qmPositions = gatherIndices(s, '?')

        def rangeChars(chStart, chEnd):
            results = []
            codeStart = ord(chStart)
            codeEnd = ord(chEnd)
            curCode = codeStart
            while curCode <= codeEnd:
                results.append(chr(curCode))
                curCode += 1
            return results

        alphabetSet = rangeChars('a', 'z')

        replacementsList = []

        def safeGetCount(dMap, keyVal):
            return dMap.get(keyVal, 0)

        def incrementCount(dMap, keyVal):
            dMap[keyVal] = safeGetCount(dMap, keyVal) + 1

        def findMinChar(countDict, charsSeq):
            minimalCount = float('inf')
            smallestChar = None
            currentCharPos = 0
            totalChars = len(charsSeq)
            while currentCharPos < totalChars:
                testChar = charsSeq[currentCharPos]
                currentCount = safeGetCount(countDict, testChar)
                if currentCount < minimalCount:
                    minimalCount = currentCount
                    smallestChar = testChar
                currentCharPos += 1
            return smallestChar

        def addReplacementForPositions(posList, countDict, alphSeq, repList):
            posIdx = 0
            posLen = len(posList)
            while posIdx < posLen:
                selectedChar = findMinChar(countDict, alphSeq)
                repList.append(selectedChar)
                incrementCount(countDict, selectedChar)
                posIdx += 1

        addReplacementForPositions(qmPositions, freqMap, alphabetSet, replacementsList)

        def sortLex(inputList):
            sortedOut = inputList[:]
            n = len(sortedOut)
            changed = True
            while changed:
                changed = False
                i = 0
                while i < n - 1:
                    if ord(sortedOut[i]) > ord(sortedOut[i + 1]):
                        sortedOut[i], sortedOut[i + 1] = sortedOut[i + 1], sortedOut[i]
                        changed = True
                    i += 1
            return sortedOut

        replacementsList = sortLex(replacementsList)

        def stringToList(strSource):
            outputList = []
            idxChar = 0
            lenStr = len(strSource)
            while idxChar < lenStr:
                outputList.append(strSource[idxChar])
                idxChar += 1
            return outputList

        mutableChars = stringToList(s)

        def replaceAtPositions(indicesList, valsList, targetList):
            cnt = 0
            lengthVals = len(valsList)
            while cnt < lengthVals:
                posRepl = indicesList[cnt]
                targetList[posRepl] = valsList[cnt]
                cnt += 1

        replaceAtPositions(qmPositions, replacementsList, mutableChars)

        def listToString(charList):
            outStr = ''
            idx = 0
            lenList = len(charList)
            while idx < lenList:
                outStr += charList[idx]
                idx += 1
            return outStr

        return listToString(mutableChars)