class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MODULO_VALUE = 10**9 + 7
        lengthArr = len(nums)
        smallest = nums[0]
        largest = nums[0]
        totalSum = 0

        for val in nums:
            if val < smallest:
                smallest = val
            if val > largest:
                largest = val
            totalSum += val

        if (cost1 << 1) <= cost2 or lengthArr < 3:
            diffSum = (largest * lengthArr) - totalSum
            return (cost1 * diffSum) % MODULO_VALUE

        def getMinCost(targetVal):
            gapMax = targetVal - smallest
            gapTotal = (targetVal * lengthArr) - totalSum
            halfGap = gapTotal // 2
            smallerPair = halfGap if halfGap < (gapTotal - gapMax) else (gapTotal - gapMax)
            return cost1 * gapTotal - 2 * cost1 * smallerPair + cost2 * smallerPair

        minimumResult = None
        candidate = largest
        limit = (2 * largest) - 1

        while candidate <= limit:
            currentCost = getMinCost(candidate)
            if minimumResult is None or currentCost < minimumResult:
                minimumResult = currentCost
            candidate += 1

        return minimumResult % MODULO_VALUE