class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MOD = 10**9 + 7
        sz = len(nums)
        low = nums[0]
        high = nums[0]
        total = 0

        idx = 0
        while idx < sz:
            el = nums[idx]
            if el < low:
                low = el
            if el > high:
                high = el
            total += el
            idx += 1

        if cost1 * 2 <= cost2 or sz < 3:
            diff = high * sz - total
            return (cost1 * diff) % MOD

        def getMinCost(target):
            gapMax = target - low
            gapTot = target * sz - total
            pairCnt = min(gapTot // 2, gapTot - gapMax)
            value = (cost1 * gapTot) - (2 * cost1 * pairCnt) + (cost2 * pairCnt)
            return value

        best = None
        key = high
        limit = 2 * high - 1

        while key <= limit:
            val = getMinCost(key)
            if best is None or val < best:
                best = val
            key += 1

        return best % MOD