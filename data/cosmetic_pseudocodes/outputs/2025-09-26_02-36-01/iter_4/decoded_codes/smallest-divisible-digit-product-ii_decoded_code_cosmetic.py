from collections import Counter

FACTOR_COUNTS = {
    0: Counter({'0': 1}),
    1: Counter(),
    2: Counter({'2': 1}),
    3: Counter({'3': 1}),
    4: Counter({'2': 2}),
    5: Counter({'5': 1}),
    6: Counter({'3': 1, '2': 1}),
    7: Counter({'7': 1}),
    8: Counter({'2': 3}),
    9: Counter({'3': 2}),
}


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeFactors, divisibleFlag = self._getPrimeCount(t)
        if not divisibleFlag:
            return "-1"

        factCount = self._getFactorCount(primeFactors)
        totalFactorsSum = sum(factCount.values())
        if totalFactorsSum > len(num):
            resultString = ""
            for primeFactor, freq in factCount.items():
                resultString += primeFactor * freq
            return resultString

        prefixCountAccumulator = Counter()
        idx = 0
        while idx < len(num):
            digitVal = int(num[idx])
            prefixCountAccumulator += FACTOR_COUNTS[digitVal]
            idx += 1

        zeroPos = len(num)
        posIndex = 0
        while posIndex < len(num) and num[posIndex] != '0':
            posIndex += 1
        if posIndex < len(num):
            zeroPos = posIndex

        if zeroPos == len(num) and all(
            primeFactors.get(int(k), 0) <= v for k, v in prefixCountAccumulator.items()
        ):
            # Check whether prefixCountAccumulator covers primeFactors
            # primeFactors keys are int keys: 2,3,5,7; prefixCountAccumulator keys are strings '2','3' etc
            # must ensure counts of each prime factor in primeFactors <= prefixCountAccumulator
            # so keys must be converted to str for prefixCountAccumulator
            # Above done: primeFactors keys int -> str, check ≤
            return num

        lengthOfNum = len(num)
        reverseIdx = lengthOfNum - 1
        while reverseIdx >= 0:
            digitChar = num[reverseIdx]
            digitInt = int(digitChar)
            prefixCountAccumulator -= FACTOR_COUNTS[digitInt]
            tailLength = (lengthOfNum - 1) - reverseIdx
            if reverseIdx <= zeroPos:
                biggerDigitGuess = digitInt + 1
                while biggerDigitGuess <= 9:
                    needed = primeFactors - prefixCountAccumulator - FACTOR_COUNTS[biggerDigitGuess]
                    newFactCount = self._getFactorCount(needed)
                    sumNewFactCount = sum(newFactCount.values())
                    if sumNewFactCount <= tailLength:
                        onesToFill = tailLength - sumNewFactCount
                        resultStart = num[:reverseIdx] if reverseIdx > 0 else ""
                        onesStr = "1" * onesToFill
                        factorsStr = ""
                        for factorKey, freq in newFactCount.items():
                            factorsStr += factorKey * freq
                        return resultStart + str(biggerDigitGuess) + onesStr + factorsStr
                    biggerDigitGuess += 1
            reverseIdx -= 1

        finalFactorCount = self._getFactorCount(primeFactors)
        sumFinalFactorValues = sum(finalFactorCount.values())
        oneCharactersCount = (len(num) + 1) - sumFinalFactorValues

        onesStringFinal = "1" * oneCharactersCount
        finalString = onesStringFinal
        for factorDigit, frequency in finalFactorCount.items():
            finalString += factorDigit * frequency

        return finalString

    def _getPrimeCount(self, t: int) -> tuple[Counter, bool]:
        primeList = [2, 3, 5, 7]
        primeCounter = Counter()
        remainderVal = t
        for primeVal in primeList:
            while remainderVal % primeVal == 0:
                remainderVal //= primeVal
                primeCounter[primeVal] += 1
        isDivisibleResult = (remainderVal == 1)
        return primeCounter, isDivisibleResult

    def _getFactorCount(self, count: Counter) -> Counter:
        twosCount = count.get(2, 0)
        eightsCount = twosCount // 3
        remainingTwos = twosCount % 3

        threesCount = count.get(3, 0)
        ninesCount = threesCount // 2
        threesRemainder = threesCount % 2

        foursCount = remainingTwos // 2
        twosRemainder = remainingTwos % 2

        sixesCount = 0

        if twosRemainder == 1 and threesRemainder == 1:
            twosRemainder = 0
            threesRemainder = 0
            sixesCount = 1
        else:
            sixesCount = 0

        if threesRemainder == 1 and foursCount == 1:
            twosRemainder = 1
            sixesCount = 1
            threesRemainder = 0
            foursCount = 0

        resultCounter = Counter()
        resultCounter['2'] = twosRemainder
        resultCounter['3'] = threesRemainder
        resultCounter['4'] = foursCount
        resultCounter['5'] = count.get(5, 0)
        resultCounter['6'] = sixesCount
        resultCounter['7'] = count.get(7, 0)
        resultCounter['8'] = eightsCount
        resultCounter['9'] = ninesCount

        return resultCounter