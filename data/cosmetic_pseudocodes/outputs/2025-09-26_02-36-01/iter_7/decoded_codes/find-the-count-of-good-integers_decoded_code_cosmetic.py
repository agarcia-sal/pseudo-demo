from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = [factorial(i) for i in range(n + 1)]

        totalCount = 0
        visitedPatterns = set()

        powBase = 1
        halfIndex = (n - 1) // 2
        for _ in range(halfIndex):
            powBase *= 10

        lowerBound = powBase
        upperBound = (powBase * 10) - 1

        currentNumber = upperBound
        while True:
            currentNumber -= 1
            if currentNumber < lowerBound:
                break

            stringNum = str(currentNumber)

            secondPartStart = n % 2
            reversedPart = stringNum[::-1][secondPartStart:]

            fullString = stringNum + reversedPart

            fullInt = int(fullString)
            if fullInt % k != 0:
                continue

            sortedString = ''.join(sorted(fullString))
            if sortedString in visitedPatterns:
                continue

            visitedPatterns.add(sortedString)

            characterFrequency = {}
            for ch in sortedString:
                characterFrequency[ch] = characterFrequency.get(ch, 0) + 1

            zeroQty = characterFrequency.get('0', 0)

            if zeroQty > 0:
                tempIndex = n - zeroQty
                # Expression simplified but preserves structure as per pseudocode
                permutationsCount = (n - (zeroQty * 1)) * factorials[n - 1]
            else:
                permutationsCount = factorials[n]

            for freqValue in characterFrequency.values():
                permutationsCount //= factorials[freqValue]

            totalCount += permutationsCount

        return totalCount