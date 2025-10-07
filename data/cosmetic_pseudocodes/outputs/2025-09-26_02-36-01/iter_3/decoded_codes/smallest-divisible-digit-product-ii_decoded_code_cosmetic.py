class Solution:
    FACTOR_COUNTS = {
        0: {}, 1: {},
        2: {2: 1},
        3: {3: 1},
        4: {2: 2},
        5: {5: 1},
        6: {2: 1, 3: 1},
        7: {7: 1},
        8: {2: 3},
        9: {3: 2},
    }

    def smallestNumber(self, num: str, t: int) -> str:
        primeNumCount, isTotallyDivisible = self._getPrimeCount(t)
        if not isTotallyDivisible:
            return "-1"

        factorNumCount = self._getFactorCount(primeNumCount)
        totalFactors = sum(factorNumCount.values())
        if totalFactors > len(num):
            resultStr = ""
            for factorStr, freqCount in factorNumCount.items():
                resultStr += factorStr * freqCount
            return resultStr

        primePrefixCount = {}
        for digitChar in num:
            digitVal = int(digitChar)
            for k, v in self.FACTOR_COUNTS.get(digitVal, {}).items():
                primePrefixCount[k] = primePrefixCount.get(k, 0) + v

        zeroPos = len(num)
        for pos, ch in enumerate(num):
            if ch == '0':
                zeroPos = pos
                break

        # If no zero found and primeCount <= primePrefixCount, return num
        if zeroPos == len(num) and self._compareCounterSum(primeNumCount, primePrefixCount) <= 0:
            return num

        idxRev = len(num) - 1
        while idxRev >= 0:
            chDigit = num[idxRev]
            intDigit = int(chDigit)
            for k in self.FACTOR_COUNTS.get(intDigit, {}):
                primePrefixCount[k] -= self.FACTOR_COUNTS[intDigit].get(k, 0)
            tailLen = (len(num) - 1) - idxRev

            if idxRev <= zeroPos:
                candidateDigit = intDigit + 1
                while candidateDigit <= 9:
                    candidatePrimeCount = {}
                    for key in primeNumCount.keys():
                        candidatePrimeCount[key] = (
                            primeNumCount[key]
                            - primePrefixCount.get(key, 0)
                            - self.FACTOR_COUNTS.get(candidateDigit, {}).get(key, 0)
                        )

                    sumCandidatePrime = sum(candidatePrimeCount.values())

                    if sumCandidatePrime <= tailLen:
                        fillOnesCount = tailLen - sumCandidatePrime
                        prefixSubstr = num[:idxRev] if idxRev > 0 else ""
                        candidateStr = prefixSubstr + str(candidateDigit) + ("1" * fillOnesCount)
                        for digitStr, freqVal in candidatePrimeCount.items():
                            candidateStr += digitStr * freqVal
                        return candidateStr
                    candidateDigit += 1
            idxRev -= 1

        factorNumCountFinal = self._getFactorCount(primeNumCount)
        sumFreq = sum(factorNumCountFinal.values())
        leadingOnesCount = (len(num) + 1) - sumFreq
        finalString = "1" * leadingOnesCount
        for k2, v2 in factorNumCountFinal.items():
            finalString += k2 * v2
        return finalString

    def _getPrimeCount(self, t: int):
        primeCounts = {}
        primesList = [2, 3, 5, 7]
        for primeNum in primesList:
            while t % primeNum == 0:
                t //= primeNum
                primeCounts[primeNum] = primeCounts.get(primeNum, 0) + 1
        successFlag = (t == 1)
        return primeCounts, successFlag

    def _getFactorCount(self, count: dict):
        twoVal = count.get(2, 0)
        threeVal = count.get(3, 0)
        fiveVal = count.get(5, 0)
        sevenVal = count.get(7, 0)

        countEight = twoVal // 3
        remTwo = twoVal % 3

        countNine = threeVal // 2
        countThreeRemainder = threeVal % 2

        countFour = remTwo // 2
        countTwoRemainder = remTwo % 2

        countSixVal = 0
        if countTwoRemainder == 1 and countThreeRemainder == 1:
            countTwoRemainder = 0
            countThreeRemainder = 0
            countSixVal = 1

        if countThreeRemainder == 1 and countFour == 1:
            countTwoRemainder = 1
            countSixVal = 1
            countThreeRemainder = 0
            countFour = 0

        return {
            "2": countTwoRemainder,
            "3": countThreeRemainder,
            "4": countFour,
            "5": fiveVal,
            "6": countSixVal,
            "7": sevenVal,
            "8": countEight,
            "9": countNine,
        }

    def _compareCounterSum(self, counterA: dict, counterB: dict) -> int:
        sumA = sum(counterA.values())
        sumB = sum(counterB.values())
        return sumA - sumB