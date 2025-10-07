class Solution:
    def minCostToEqualizeArray(self, inputArray, rateA, rateB):
        MODULUS = 1_000_000_007
        length = len(inputArray)
        minimumValue = inputArray[0]
        maximumValue = inputArray[0]
        totalSum = 0

        index = 0
        while index < length:
            totalSum += inputArray[index]
            if inputArray[index] < minimumValue:
                minimumValue = inputArray[index]
            if inputArray[index] > maximumValue:
                maximumValue = inputArray[index]
            index += 1

        if (rateA * 2 <= rateB) or (length < 3):
            gapTotal = (maximumValue * length) - totalSum
            return (gapTotal * rateA) % MODULUS

        def getMinCost(target):
            maxGapValue = target - minimumValue
            totalGap = (target * length) - totalSum
            minPairs = totalGap // 2
            if minPairs > totalGap - maxGapValue:
                minPairs = totalGap - maxGapValue
            costCalculation = (totalGap * rateA) - (2 * minPairs * rateA) + (minPairs * rateB)
            return costCalculation

        bestCost = getMinCost(maximumValue)
        candidate = maximumValue + 1
        upperBound = 2 * maximumValue

        while candidate < upperBound:
            currentCost = getMinCost(candidate)
            if currentCost < bestCost:
                bestCost = currentCost
            candidate += 1

        return bestCost % MODULUS