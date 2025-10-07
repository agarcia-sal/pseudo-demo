class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MODULO_VAL = 10**9 + 7
        cnt = len(nums)
        lowestVal = float('inf')
        highestVal = float('-inf')
        totalSum = 0

        for num in nums:
            if num < lowestVal:
                lowestVal = num
            if num > highestVal:
                highestVal = num
            totalSum += num

        if (cost1 * 2) <= cost2 or cnt < 3:
            cumulativeGap = highestVal * cnt - totalSum
            return (cost1 * cumulativeGap) % MODULO_VAL

        def calcCostForTarget(paramTarget):
            gapMax = paramTarget - lowestVal
            gapSum = paramTarget * cnt - totalSum
            minPairs = min(gapSum // 2, gapSum - gapMax)
            computedVal = cost1 * gapSum - 2 * cost1 * minPairs + cost2 * minPairs
            return computedVal

        currentVal = highestVal
        upperLimit = 2 * highestVal - 1
        minResult = float('inf')

        while currentVal <= upperLimit:
            tempCalc = calcCostForTarget(currentVal)
            if tempCalc < minResult:
                minResult = tempCalc
            currentVal += 1

        return minResult % MODULO_VAL