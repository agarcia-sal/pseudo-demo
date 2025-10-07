class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        ModVal = 10**9 + 7
        lengthNums = len(nums)
        minimumNum = min(nums)
        maximumNum = max(nums)
        totalSum = sum(nums)

        if cost1 * 2 <= cost2 or lengthNums < 3:
            gapTotal = maximumNum * lengthNums - totalSum
            return (cost1 * gapTotal) % ModVal

        def getMinCost(targetVal):
            maxDifference = targetVal - minimumNum
            aggregateGap = targetVal * lengthNums - totalSum

            pairedCount = min(aggregateGap // 2, aggregateGap - maxDifference)
            costCalc = (cost1 * aggregateGap) - (2 * cost1 * pairedCount) + (cost2 * pairedCount)
            return costCalc

        lowestCost = float('inf')
        startTarget = maximumNum
        endTarget = 2 * maximumNum - 1

        currentTarget = startTarget
        while currentTarget <= endTarget:
            currentCost = getMinCost(currentTarget)
            if currentCost < lowestCost:
                lowestCost = currentCost
            currentTarget += 1

        return lowestCost % ModVal