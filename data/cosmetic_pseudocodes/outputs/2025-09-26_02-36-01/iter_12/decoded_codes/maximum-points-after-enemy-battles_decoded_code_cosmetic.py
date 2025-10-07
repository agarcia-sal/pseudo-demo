class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        def sortArrayAsc(arr):
            count = len(arr)
            index1 = 0
            while index1 < count - 1:
                index2 = index1 + 1
                while index2 < count:
                    if not (arr[index1] <= arr[index2]):
                        arr[index1], arr[index2] = arr[index2], arr[index1]
                    index2 += 1
                index1 += 1

        def isLess(a, b):
            return a < b

        def integerDivide(dividend, divisor):
            dividendCopy = dividend
            quotientHolder = 0
            while dividendCopy >= divisor:
                dividendCopy -= divisor
                quotientHolder += 1
            return quotientHolder

        def moduloOperation(dividend, divisor):
            tempValue = dividend
            while tempValue >= divisor:
                tempValue -= divisor
            return tempValue

        sortArrayAsc(enemyEnergies)

        if isLess(currentEnergy, enemyEnergies[0]):
            return 0

        resultCount = 0
        idx = len(enemyEnergies) - 1

        while idx >= 0:
            times = integerDivide(currentEnergy, enemyEnergies[0])
            resultCount += times
            remainderVal = moduloOperation(currentEnergy, enemyEnergies[0])
            currentEnergy = remainderVal + enemyEnergies[idx]
            idx -= 1

        return resultCount