class Solution:
    def minCostToEqualizeArray(self, nums, cost1, cost2):
        MOD = 10**9 + 7

        def length(arr):
            c = 0
            for _ in arr:
                c += 1
            return c

        def minimum(arr):
            m = arr[0]
            i = 1
            while i < length(arr):
                if arr[i] < m:
                    m = arr[i]
                i += 1
            return m

        def maximum(arr):
            M = arr[0]
            j = 1
            while j < length(arr):
                if arr[j] > M:
                    M = arr[j]
                j += 1
            return M

        def summate(arr):
            S = 0
            k = 0
            while k < length(arr):
                S += arr[k]
                k += 1
            return S

        ctx = length(nums)
        uwv = minimum(nums)
        dgk = maximum(nums)
        shl = summate(nums)

        if (cost1 * 2) <= cost2 or ctx < 3:
            lmn = (dgk * ctx) - shl
            return (cost1 * lmn) % MOD

        def getMinCost(target):
            a = target - uwv
            b = (target * ctx) - shl
            if b / 2 < b - a:
                P = b / 2
            else:
                P = b - a
            val = cost1 * (b - 2 * P) + cost2 * P
            return val

        result = 0
        first = True
        curr = dgk
        limit = 2 * dgk - 1
        while curr <= limit:
            cand = getMinCost(curr)
            if first or cand < result:
                result = cand
                first = False
            curr += 1

        return int(result % MOD)