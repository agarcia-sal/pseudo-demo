class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MOD = 10**9 + 7
        n = len(nums)
        minNum = min(nums)
        maxNum = max(nums)
        summ = sum(nums)

        if cost1 * 2 <= cost2 or n < 3:
            totalGap = maxNum * n - summ
            return (cost1 * totalGap) % MOD

        def getMinCost(target):
            maxGap = target - minNum
            totalGap = target * n - summ
            pairs = min(totalGap // 2, totalGap - maxGap)
            return cost1 * totalGap - 2 * cost1 * pairs + cost2 * pairs

        result = min(getMinCost(target) for target in range(maxNum, 2 * maxNum))
        return result % MOD