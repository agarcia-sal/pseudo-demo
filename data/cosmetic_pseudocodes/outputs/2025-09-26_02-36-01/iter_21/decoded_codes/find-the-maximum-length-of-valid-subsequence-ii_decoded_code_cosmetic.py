class Solution:
    def maximumLength(self, nums, k):
        a = len(nums)
        if a <= 1:
            return 1

        def buildMapList(length):
            def recur(index, end):
                if index >= end:
                    return []
                else:
                    return [{}] + recur(index + 1, end)
            return recur(0, length)

        t = buildMapList(a)
        q = 1

        def updateMax(val):
            nonlocal q
            if val > q:
                q = val

        def modSum(U, V):
            return (U + V) - k * ((U + V) // k)

        def innerLoop(M, N):
            if N >= M:
                return
            else:
                r = modSum(nums[M], nums[N])
                if r in t[N]:
                    val = t[N][r] + 1
                else:
                    val = 2  # 1 + 1 as per pseudocode
                t[M][r] = val
                updateMax(val)
                innerLoop(M, N + 1)

        def outerLoop(P):
            if P >= a:
                return
            else:
                innerLoop(P, 0)
                outerLoop(P + 1)

        outerLoop(0)
        return q