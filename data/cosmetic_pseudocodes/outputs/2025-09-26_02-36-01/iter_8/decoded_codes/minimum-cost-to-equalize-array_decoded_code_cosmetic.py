class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        LimitValue = 10**9 + 7
        lengthVar = len(nums)
        baseVal = min(nums)
        apexVal = max(nums)
        aggregateSum = sum(nums)

        if (cost1 * 2) <= cost2 or lengthVar < 3:
            gapTotal = apexVal * lengthVar - aggregateSum
            return (cost1 * gapTotal) % LimitValue
        else:
            def getMinCost(target):
                gapMax = target - baseVal
                gapSum = target * lengthVar - aggregateSum
                # pairCount calculation as minimum of integer division and subtraction result
                pairCount = min(gapSum // 2, gapSum - gapMax)
                costCalcPartOne = cost1 * gapSum
                costCalcPartTwo = 2 * pairCount
                costCalcPartThree = cost2 * pairCount
                costFinal = costCalcPartOne - costCalcPartTwo + costCalcPartThree
                return costFinal

            resTemp = getMinCost(apexVal)
            currentTarget = apexVal + 1
            limitTarget = (2 * apexVal) - 1

            while currentTarget <= limitTarget:
                newCost = getMinCost(currentTarget)
                if newCost < resTemp:
                    resTemp = newCost
                currentTarget += 1

            return resTemp % LimitValue