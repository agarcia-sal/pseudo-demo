class Solution:
    def minCostToEqualizeArray(self, inputList, valA, valB):
        MOD_VALUE = 10**9 + 7
        lengthList = len(inputList)

        smallestVal = inputList[0]
        largestVal = inputList[0]
        sumVals = 0

        def findBoundsAndSum(i, accumMin, accumMax, accumSum):
            if i == lengthList:
                return accumMin, accumMax, accumSum
            currentElem = inputList[i]
            newMin = accumMin if currentElem >= accumMin else currentElem
            newMax = accumMax if currentElem <= accumMax else currentElem
            return findBoundsAndSum(i + 1, newMin, newMax, accumSum + currentElem)

        smallestVal, largestVal, sumVals = findBoundsAndSum(0, smallestVal, largestVal, 0)

        if (valA * 2) <= valB or lengthList < 3:
            totalDiff = (largestVal * lengthList) - sumVals
            outcome = valA * totalDiff
            finalResult = outcome % MOD_VALUE
            return finalResult

        def computeCostForTarget(targetVal):
            gapMax = targetVal - smallestVal
            overallGap = (targetVal * lengthList) - sumVals

            pairsCount1 = overallGap // 2
            pairsCount2 = overallGap - gapMax
            pairsCount = pairsCount1 if pairsCount1 <= pairsCount2 else pairsCount2

            partOne = valA * overallGap
            partTwo = 2 * pairsCount
            partThree = valB * pairsCount
            totalCost = partOne - partTwo + partThree
            return totalCost

        def rangeMinValue(low, high, currentMin):
            if low > high:
                return currentMin
            valCurr = computeCostForTarget(low)
            newMin = valCurr if valCurr < currentMin else currentMin
            return rangeMinValue(low + 1, high, newMin)

        upperBound = (2 * largestVal) - 1
        minimalCostFinal = rangeMinValue(largestVal, upperBound, 9223372036854775807)
        answerFinal = minimalCostFinal % MOD_VALUE
        return answerFinal