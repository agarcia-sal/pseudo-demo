class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        CONST_MOD_VALUE = 10**9 + 7
        lenVal = len(nums)
        lowBound = nums[0]
        highBound = nums[0]
        totalSum = 0

        for idx in range(lenVal):
            val = nums[idx]
            if val < lowBound:
                lowBound = val
            if val > highBound:
                highBound = val
            totalSum += val

        if (cost1 * 2) <= cost2 or lenVal < 3:
            gapSum = (highBound * lenVal) - totalSum
            return (cost1 * gapSum) % CONST_MOD_VALUE

        def getMinCost(target):
            diffMax = target - lowBound
            diffTotal = (target * lenVal) - totalSum
            pairCount = diffTotal // 2
            if pairCount > diffTotal - diffMax:
                pairCount = diffTotal - diffMax
            costCalc = (cost1 * diffTotal) - (2 * cost1 * pairCount) + (cost2 * pairCount)
            return costCalc

        iterVal = highBound
        minResult = getMinCost(iterVal)
        while iterVal < (2 * highBound - 1):
            iterVal += 1
            valToCheck = getMinCost(iterVal)
            if valToCheck < minResult:
                minResult = valToCheck

        return minResult % CONST_MOD_VALUE