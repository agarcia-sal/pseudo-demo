class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MODULO_VAL = 10**9 + 7

        lengthVal = len(nums)

        minimumElement = min(nums)
        maximumElement = max(nums)
        sumElements = sum(nums)

        if not (cost1 + cost1 <= cost2) or lengthVal < 3:
            totalDiff = maximumElement * lengthVal - sumElements
            res = cost1 * totalDiff
            return res % MODULO_VAL
        else:
            def getMinCost(target):
                diffMax = target - minimumElement
                diffTotal = target * lengthVal - sumElements
                pairCount = diffTotal // 2
                if diffTotal - diffMax < pairCount:
                    pairCount = diffTotal - diffMax
                return cost1 * diffTotal - 2 * cost1 * pairCount + cost2 * pairCount

            minimalCost = getMinCost(maximumElement)
            for iter_val in range(maximumElement, 2 * maximumElement):
                possibleResult = getMinCost(iter_val)
                if possibleResult < minimalCost:
                    minimalCost = possibleResult

            return minimalCost % MODULO_VAL