from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),  # digit 0 contributes no prime factors for the problem context
    1: Counter(),
    2: Counter({2: 1}),
    3: Counter({3: 1}),
    4: Counter({2: 2}),
    5: Counter({5: 1}),
    6: Counter({3: 1, 2: 1}),
    7: Counter({7: 1}),
    8: Counter({2: 3}),
    9: Counter({3: 2}),
}

class Solution:
    def smallestNumber(self, originalStr: str, divisor: int) -> str:
        def primeDecomposition(divde):
            return self._getPrimeCount(divde)

        primeFactCounts, canDivideFlag = primeDecomposition(divisor)
        if not canDivideFlag:
            return "-1"

        factorsFrequency = self._getFactorCount(primeFactCounts)

        def sumValues(cnt):
            total = 0
            keysList = list(cnt.keys())
            idx = 0
            while idx < len(keysList):
                keyName = keysList[idx]
                total += cnt[keyName]
                idx += 1
            return total

        if sumValues(factorsFrequency) > len(originalStr):
            def composeStr(freqMap):
                resultStr = ""
                digitsList = list(freqMap.keys())
                cursor = 0
                while True:
                    if cursor >= len(digitsList):
                        break
                    currentDigit = digitsList[cursor]
                    countDigit = freqMap[currentDigit]
                    repStr = ""
                    countIter = 0
                    while countIter < countDigit:
                        repStr += currentDigit
                        countIter += 1
                    resultStr += repStr
                    cursor += 1
                return resultStr
            return composeStr(factorsFrequency)

        def accumulateFactorCounts(s):
            accCounter = Counter()

            def intCharToInt(ch):
                return ord(ch) - ord('0')

            position = 0
            while position < len(s):
                numberVal = intCharToInt(s[position])
                accCounter += FACTOR_COUNTS[numberVal]
                position += 1
            return accCounter

        primeFactPrefixSum = accumulateFactorCounts(originalStr)

        def findFirstZeroIndex(s):
            posIdx = 0
            while True:
                if posIdx >= len(s):
                    return len(s)
                if s[posIdx] == '0':
                    return posIdx
                posIdx += 1

        firstZeroPosition = findFirstZeroIndex(originalStr)

        # Compare primeFactCounts <= primeFactPrefixSum
        # For Counter a <= Counter b means for every key, a[key] <= b[key]
        def counter_leq(a: Counter, b: Counter) -> bool:
            for key, val in a.items():
                if val > b.get(key, 0):
                    return False
            return True

        if firstZeroPosition == len(originalStr) and counter_leq(primeFactCounts, primeFactPrefixSum):
            return originalStr

        def intCharVal(ch):
            return ord(ch) - ord('0')

        def sumCounterValues(cnt):
            valsSum = 0
            keysArray = list(cnt.keys())
            iCursor = 0
            while iCursor < len(keysArray):
                valsSum += cnt[keysArray[iCursor]]
                iCursor += 1
            return valsSum

        def strRepeat(ch, times):
            # Iterative to avoid recursion limit
            return ch * times if times > 0 else ""

        lenNum = len(originalStr)

        def composeFactorsRepeated(freqCounts):
            outStr = ""
            keysArr = list(freqCounts.keys())
            idxCtr = 0
            while True:
                if idxCtr >= len(keysArr):
                    break
                keyChar = keysArr[idxCtr]
                repCount = freqCounts[keyChar]
                while repCount > 0:
                    outStr += keyChar
                    repCount -= 1
                idxCtr += 1
            return outStr

        def tryIncreasingDigit(pos, charDigit, prefixSum):
            if pos > firstZeroPosition:
                return None
            searchVal = charDigit + 1
            while searchVal <= 9:
                diffCount = primeFactCounts - prefixSum - FACTOR_COUNTS[searchVal]
                nextFactorFreqs = self._getFactorCount(diffCount)
                if sumCounterValues(nextFactorFreqs) <= (lenNum - 1 - pos):
                    neededOnes = (lenNum - 1 - pos) - sumCounterValues(nextFactorFreqs)
                    prefixSubstr = originalStr[:pos]
                    return prefixSubstr + str(searchVal) + strRepeat('1', neededOnes) + composeFactorsRepeated(nextFactorFreqs)
                searchVal += 1
            return None

        def searchLoop(idx):
            if idx < 0:
                return None
            dNum = intCharVal(originalStr[idx])
            # subtract FACTOR_COUNTS[dNum] from primeFactPrefixSum
            primeFactPrefixSum.subtract(FACTOR_COUNTS[dNum])
            # Clean zero or negative counts for safety
            for k in list(primeFactPrefixSum.keys()):
                if primeFactPrefixSum[k] <= 0:
                    del primeFactPrefixSum[k]
            if idx <= firstZeroPosition:
                resAttempt = tryIncreasingDigit(idx, dNum, primeFactPrefixSum)
                if resAttempt is not None:
                    return resAttempt
            return searchLoop(idx - 1)

        searchStartIndex = len(originalStr) - 1
        finalTry = searchLoop(searchStartIndex)
        if finalTry is not None:
            return finalTry

        factCountFinal = self._getFactorCount(primeFactCounts)
        sumFactVals = sumCounterValues(factCountFinal)
        return strRepeat('1', (len(originalStr) + 1) - sumFactVals) + composeFactorsRepeated(factCountFinal)

    def _getPrimeCount(self, dividend):
        countersMap = Counter()
        primesList = [2, 3, 5, 7]

        def divPrimeLoop(index, val, countDict):
            if index >= len(primesList):
                return countDict, val == 1
            pnum = primesList[index]
            if val % pnum == 0:
                newVal = val // pnum
                countDict[pnum] = countDict.get(pnum, 0) + 1
                return divPrimeLoop(index, newVal, countDict)
            else:
                return divPrimeLoop(index + 1, val, countDict)

        return divPrimeLoop(0, dividend, countersMap)

    def _getFactorCount(self, cnt: Counter) -> Counter:
        twosCntTotal = cnt.get(2, 0)
        threesCntTotal = cnt.get(3, 0)
        count8Val = twosCntTotal // 3
        remain2Val = twosCntTotal % 3
        count9Val = threesCntTotal // 2
        count3Val = threesCntTotal % 2
        count4Val = remain2Val // 2
        count2Val = remain2Val % 2
        count6Val = 0
        if count2Val == 1 and count3Val == 1:
            count2Val = 0
            count3Val = 0
            count6Val = 1
        if count3Val == 1 and count4Val == 1:
            count2Val = 1
            count6Val = 1
            count3Val = 0
            count4Val = 0
        counterResult = Counter()
        counterResult['2'] = count2Val
        counterResult['3'] = count3Val
        counterResult['4'] = count4Val
        counterResult['5'] = cnt.get(5, 0)
        counterResult['6'] = count6Val
        counterResult['7'] = cnt.get(7, 0)
        counterResult['8'] = count8Val
        counterResult['9'] = count9Val
        # Filter out zero counts for cleanliness
        return +counterResult  # +Counter removes zero and negative counts