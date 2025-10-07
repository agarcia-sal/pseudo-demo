from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        def computeFreq(vals, idx, oddSumAcc, evenSumAcc):
            if idx < 0:
                return oddSumAcc + evenSumAcc
            currVal = vals[idx]
            isCurrOdd = (currVal % 2) == 1
            isCurrEvenAndNonZero = (currVal % 2) == 0 and currVal != 0
            newOddSum = oddSumAcc
            newEvenSum = evenSumAcc
            if isCurrOdd:
                newOddSum += 1
            if isCurrEvenAndNonZero:
                newEvenSum += 2  # sum of 1 + 1
            return computeFreq(vals, idx - 1, newOddSum, newEvenSum)

        frequencyMap = Counter(s)
        valsCollection = list(frequencyMap.values())
        lastIndex = len(valsCollection) - 1
        aggregateResult = computeFreq(valsCollection, lastIndex, 0, 0)
        return aggregateResult