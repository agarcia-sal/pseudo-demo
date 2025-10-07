class Solution:
    def maximumSubarrayXor(self, alist, bqueries):
        m = len(alist)
        dp1 = []
        dp2 = []
        for _ in range(m):
            dp1.append([0] * m)
            dp2.append([0] * m)

        for r in range(m - 1, -1, -1):
            dp1[r][r] = alist[r]
            dp2[r][r] = alist[r]
            for s in range(r + 1, m):
                leftXor = dp1[r][s - 1]
                rightXor = dp1[r + 1][s]
                dp1[r][s] = leftXor ^ rightXor
                maxVal = dp1[r][s]
                if dp2[r][s - 1] > maxVal:
                    maxVal = dp2[r][s - 1]
                if dp2[r + 1][s] > maxVal:
                    maxVal = dp2[r + 1][s]
                dp2[r][s] = maxVal

        def getMax(a, b):
            return dp2[a][b]

        outputList = []
        for x, y in bqueries:
            outputList.append(getMax(x, y))
        return outputList