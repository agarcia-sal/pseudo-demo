from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter({2: 1}),
    3: Counter({3: 1}),
    4: Counter({2: 2}),
    5: Counter({5: 1}),
    6: Counter({2: 1, 3: 1}),
    7: Counter({7: 1}),
    8: Counter({2: 3}),
    9: Counter({3: 2}),
}

class Solution:
    def smallestNumber(self, originalString: str, factorParam: int) -> str:
        alphaCounts, divisionFlag = self._getPrimeCount(factorParam)
        if not divisionFlag:
            return "-1"

        betaCounts = self._getFactorCount(alphaCounts)
        if sum(betaCounts.values()) > len(originalString):
            resultString = []
            for key in betaCounts:
                resultString.append(key * betaCounts[key])
            return "".join(resultString)

        prefixSum = Counter()
        for char in originalString:
            digitVal = ord(char) - ord('0')
            prefixSum += FACTOR_COUNTS[digitVal]

        zeroPos = len(originalString)
        for posIndex, ch in enumerate(originalString):
            if ch == '0':
                zeroPos = posIndex
                break

        if zeroPos == len(originalString) and all(prefixSum[k] >= alphaCounts.get(k, 0) for k in alphaCounts):
            return originalString

        lengthStr = len(originalString)
        revIndex = lengthStr - 1

        while revIndex >= 0:
            currentDigit = ord(originalString[revIndex]) - ord('0')
            prefixSum -= FACTOR_COUNTS[currentDigit]
            availableSpaces = lengthStr - 1 - revIndex

            if revIndex <= zeroPos:
                testDigit = currentDigit + 1
                while testDigit <= 9:
                    diff = Counter(alphaCounts) - prefixSum - FACTOR_COUNTS[testDigit]
                    # Negative counts in diff are set to zero for _getFactorCount input consistency
                    for k in list(diff):
                        if diff[k] < 0:
                            diff[k] = 0
                    updatedCounts = self._getFactorCount(diff)
                    if sum(updatedCounts.values()) <= availableSpaces:
                        fillCount = availableSpaces - sum(updatedCounts.values())
                        answerList = list(originalString[:revIndex]) + [str(testDigit)] + ["1"] * fillCount
                        for key in updatedCounts:
                            answerList.append(key * updatedCounts[key])
                        return "".join(answerList)
                    testDigit += 1
            revIndex -= 1

        betaCountsFinal = self._getFactorCount(alphaCounts)
        totalFill = lengthStr + 1 - sum(betaCountsFinal.values())
        outputList = ["1"] * totalFill
        for key in betaCountsFinal:
            outputList.append(key * betaCountsFinal[key])
        return "".join(outputList)

    def _getPrimeCount(self, inputVal: int) -> tuple[Counter, bool]:
        countMap = Counter()
        primes = [2,3,5,7]
        for primeVal in primes:
            while inputVal % primeVal == 0:
                inputVal //= primeVal
                countMap[primeVal] += 1
        return countMap, (inputVal == 1)

    def _getFactorCount(self, factors: Counter) -> dict:
        # Extract counts with default 0
        c2 = factors.get(2,0)
        c3 = factors.get(3,0)
        c5 = factors.get(5,0)
        c7 = factors.get(7,0)

        div2 = c2 // 3
        rem2 = c2 % 3
        div3 = c3 // 2
        rem3 = c3 % 2
        countFour = rem2 // 2
        countTwo = rem2 % 2
        countSix = 0

        if countTwo == 1 and rem3 == 1:
            countTwo = 0
            rem3 = 0
            countSix = 1

        if rem3 == 1 and countFour == 1:
            countTwo = 1
            countSix = 1
            rem3 = 0
            countFour = 0

        return {
            "2": countTwo,
            "3": rem3,
            "4": countFour,
            "5": c5,
            "6": countSix,
            "7": c7,
            "8": div2,
            "9": div3,
        }