class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MODULO_VALUE = 10**9 + 7
        length = len(nums)
        lowerBound = nums[0]
        upperBound = nums[0]
        aggregate = 0

        def findBoundsAndSum(idx):
            nonlocal lowerBound, upperBound, aggregate
            if idx == length:
                return
            val = nums[idx]
            if val < lowerBound:
                lowerBound = val
            if val > upperBound:
                upperBound = val
            aggregate += val
            findBoundsAndSum(idx + 1)

        findBoundsAndSum(0)

        if cost1 * 2 <= cost2 or length < 3:
            gapSum = upperBound * length - aggregate
            return (cost1 * gapSum) % MODULO_VALUE

        def computeExpense(target):
            maxDiff = target - lowerBound
            totalDifference = target * length - aggregate
            paired = totalDifference // 2
            if paired > totalDifference - maxDiff:
                paired = totalDifference - maxDiff
            return cost1 * totalDifference - 2 * cost1 * paired + cost2 * paired

        def findMinimumExpense(currTarget, currResult):
            if currTarget > 2 * upperBound - 1:
                return currResult
            currentCost = computeExpense(currTarget)
            newResult = currResult
            if currentCost < newResult:
                newResult = currentCost
            return findMinimumExpense(currTarget + 1, newResult)

        minimalCost = findMinimumExpense(upperBound, 9223372036854775807)
        return minimalCost % MODULO_VALUE