class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def computeFactorialArray(m: int) -> list[int]:
            result = []
            idx = 0
            while idx < m + 1:
                appendFactorial(idx, result)
                idx += 1
            return result

        def appendFactorial(value: int, arr: list[int]) -> None:
            if value == 0:
                arr.append(1)
                return
            acc = 1
            counter = value
            while counter > 0:
                acc *= counter
                counter -= 1
            arr.append(acc)

        def reverseString(inputString: str) -> str:
            outputString = ""
            pos = len(inputString) - 1
            while pos >= 0:
                outputString += inputString[pos]
                pos -= 1
            return outputString

        def substring(orig: str, startPos: int) -> str:
            resultString = ""
            iter_ = startPos
            while iter_ < len(orig):
                resultString += orig[iter_]
                iter_ += 1
            return resultString

        def stringToInteger(s: str) -> int:
            resInt = 0
            power = 1
            indexPos = len(s) - 1
            while indexPos >= 0:
                charCode = ord(s[indexPos]) - ord('0')
                resInt += charCode * power
                power *= 10
                indexPos -= 1
            return resInt

        def modIsZero(val: int, modBy: int) -> bool:
            moduloRes = val
            while moduloRes >= modBy:
                moduloRes -= modBy
            return moduloRes == 0

        def simpleSort(listToSort: list[str]) -> None:
            iVar = 0
            length = len(listToSort)
            while iVar < length - 1:
                jVar = iVar + 1
                while jVar < length:
                    if listToSort[iVar] > listToSort[jVar]:
                        listToSort[iVar], listToSort[jVar] = listToSort[jVar], listToSort[iVar]
                    jVar += 1
                iVar += 1

        def sortCharactersAsc(strInput: str) -> str:
            charList = []
            ptr = 0
            while ptr < len(strInput):
                charList.append(strInput[ptr])
                ptr += 1
            simpleSort(charList)
            sortedStr = ""
            idx2 = 0
            while idx2 < len(charList):
                sortedStr += charList[idx2]
                idx2 += 1
            return sortedStr

        def countCharacters(freqStr: str) -> dict[str, int]:
            frequencyMap = {}
            ctr1 = 0
            while ctr1 < len(freqStr):
                currentChar = freqStr[ctr1]
                if currentChar not in frequencyMap:
                    frequencyMap[currentChar] = 0
                frequencyMap[currentChar] += 1
                ctr1 += 1
            return frequencyMap

        factorials = computeFactorialArray(n)

        finalAns = 0
        visitedMap = {}

        baseNum = 1
        expCounter = (n - 1) // 2
        expChecker = 0
        while expChecker < expCounter:
            baseNum *= 10
            expChecker += 1

        endLimit = baseNum * 10 - 1
        curVal = baseNum

        while curVal <= endLimit:
            strRepr = str(curVal)
            strRev = reverseString(strRepr)
            tailStart = n % 2
            strSuf = substring(strRev, tailStart)
            fullStr = strRepr + strSuf
            if not modIsZero(stringToInteger(fullStr), k):
                curVal += 1
                continue

            sortedStr = sortCharactersAsc(fullStr)
            if sortedStr in visitedMap:
                curVal += 1
                continue

            visitedMap[sortedStr] = True
            freqCount = countCharacters(sortedStr)

            hasZeroChar = False
            zeroCountVal = 0
            if '0' in freqCount:
                if freqCount['0'] > 0:
                    hasZeroChar = True
                    zeroCountVal = freqCount['0']

            if hasZeroChar:
                partialRes = (n - zeroCountVal) * factorials[n - 1]
            else:
                partialRes = factorials[n]

            freqVals = []
            freqIter = 0
            for keyVal in freqCount.keys():
                freqVals.append(freqCount[keyVal])
                freqIter += 1

            divideIter = 0
            while divideIter < len(freqVals):
                partialRes //= factorials[freqVals[divideIter]]
                divideIter += 1

            finalAns += partialRes
            curVal += 1

        return finalAns