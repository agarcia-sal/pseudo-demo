class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MODULUS = 10**9 + 7
        length = len(nums)
        smallest = min(nums)
        largest = max(nums)
        sumValues = sum(nums)

        if cost1 * 2 <= cost2 or length < 3:
            gapSum = largest * length - sumValues
            return (cost1 * gapSum) % MODULUS

        def computeCost(target):
            gapMax = target - smallest
            gapSumTotal = target * length - sumValues
            pairsUsed = min(gapSumTotal // 2, gapSumTotal - gapMax)
            costCalculation = cost1 * gapSumTotal - 2 * pairsUsed * cost1 + cost2 * pairsUsed
            return costCalculation

        answer = float('inf')
        for candidate in range(largest, 2 * largest):
            currentCost = computeCost(candidate)
            if currentCost < answer:
                answer = currentCost

        return answer % MODULUS