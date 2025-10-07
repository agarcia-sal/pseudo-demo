class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MOD_CONST = 10**9 + 7

        lengthNums = len(nums)

        minElem = nums[0]
        maxElem = nums[0]
        for i in range(1, lengthNums):
            if nums[i] < minElem:
                minElem = nums[i]
            if nums[i] > maxElem:
                maxElem = nums[i]

        sumElems = sum(nums)

        shortcutCheck = (cost1 * 2) <= cost2
        if shortcutCheck or lengthNums < 3:
            totalDiff = (maxElem * lengthNums) - sumElems
            return (cost1 * totalDiff) % MOD_CONST

        def getMinCost(target):
            gapMax = target - minElem
            totalGapCalc = (target * lengthNums) - sumElems

            if totalGapCalc / 2 < totalGapCalc - gapMax:
                minPairValue = totalGapCalc / 2
            else:
                minPairValue = totalGapCalc - gapMax

            pairCount = minPairValue

            costCalc = (cost1 * totalGapCalc) - (2 * cost1 * pairCount) + (cost2 * pairCount)
            return costCalc

        result = getMinCost(maxElem)
        currentTarget = maxElem + 1
        while currentTarget < (2 * maxElem):
            candidateCost = getMinCost(currentTarget)
            if candidateCost < result:
                result = candidateCost
            currentTarget += 1

        adjustedResult = result % MOD_CONST
        return adjustedResult