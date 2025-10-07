class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        P = 10**9 + 7
        u = len(nums)
        a = nums[0]
        i = 1
        while i < u:
            if nums[i] < a:
                a = nums[i]
            i += 1
        d = nums[0]
        j = 1
        while j < u:
            if nums[j] > d:
                d = nums[j]
            j += 1
        s = 0
        k = 0
        while k < u:
            s += nums[k]
            k += 1

        if (cost1 * 2) <= cost2 or u < 3:
            v = (d * u) - s
            return (cost1 * v) % P

        def getMinCost(target):
            e = target - a
            f = (target * u) - s
            h = f / 2
            g = f - e
            m = min(h, g)
            return (cost1 * f) - (2 * m * cost1) + (cost2 * m)

        w = max(0, 2 * d - 1)
        best = getMinCost(d)
        l = d + 1
        while l <= w:
            candidate = getMinCost(l)
            if candidate < best:
                best = candidate
            l += 1

        return best % P