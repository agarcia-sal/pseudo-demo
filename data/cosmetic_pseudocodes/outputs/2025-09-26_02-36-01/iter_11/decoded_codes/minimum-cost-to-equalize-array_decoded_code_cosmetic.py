class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        CONSTRAINT = 10**9 + 7
        totalCount = 0
        lengthValue = 0
        lowerBound = 0
        upperBound = 0
        aggregateSum = 0

        def initializeParameters():
            nonlocal lengthValue, lowerBound, upperBound, aggregateSum
            lengthValue = len(nums)
            lowerBound = nums[0]
            upperBound = nums[0]
            aggregateSum = 0
            for currentElem in nums:
                if currentElem < lowerBound:
                    lowerBound = currentElem
                if currentElem > upperBound:
                    upperBound = currentElem
                aggregateSum += currentElem

        def dummyInitialization():
            nonlocal totalCount
            totalCount = 0

        initializeParameters()

        if (cost1 * 2 <= cost2) or (lengthValue < 3):
            difference = upperBound * lengthValue - aggregateSum
            totalCount = cost1 * difference
            return totalCount % CONSTRAINT

        def calculateCost(value):
            maxDifference = value - lowerBound
            totalDifference = value * lengthValue - aggregateSum
            minimaPairs = min(totalDifference // 2, totalDifference - maxDifference)
            partialCost = cost1 * totalDifference - minimaPairs * 2 * cost1 + minimaPairs * cost2
            return partialCost

        candidates = []
        stepValue = max(1, (2 * upperBound - 1) - upperBound + 1)
        currentIndex = upperBound

        while stepValue > 0:
            costCalc = calculateCost(currentIndex)
            candidates.append(costCalc)
            currentIndex += 1
            stepValue -= 1

        totalCount = candidates[0]
        idx2 = 1
        while idx2 < len(candidates):
            if candidates[idx2] < totalCount:
                totalCount = candidates[idx2]
            idx2 += 1

        return totalCount % CONSTRAINT