class Solution:
    def maxCollectedFruits(self, fruits):
        nVar = len(fruits)

        dirAlpha = [(1, 1), (0, 1)]
        dirBeta = [(1, 0), (1, 1), (1, -1)]
        dirGamma = [(-1, 1), (0, 1), (1, 1)]

        memoMap = {}

        def dp(a1, b1, a2, b2, a3, b3):
            def isValidPosition(p, limit):
                return 0 <= p < limit

            if not (isValidPosition(a1, nVar) and isValidPosition(b1, nVar) and
                    isValidPosition(a2, nVar) and isValidPosition(b2, nVar) and
                    isValidPosition(a3, nVar) and isValidPosition(b3, nVar)):
                return -10**10  # large negative number as negative infinity substitute

            lastIndex = nVar - 1
            if (a1 == b1 == a2 == b2 == a3 == b3 == lastIndex):
                return fruits[lastIndex][lastIndex]

            keyTuple = (a1, b1, a2, b2, a3, b3)
            if keyTuple in memoMap:
                return memoMap[keyTuple]

            collectedSum = fruits[b1][a1]

            # If first two positions coincide
            if (a1 == a2 and b1 == b2) or (a1 == a3 and b1 == b3):
                collectedSum = 0

            if a2 == a3 and b2 == b3:
                collectedSum += fruits[b2][a2]
            else:
                collectedSum += fruits[b2][a2] + fruits[b3][a3]

            maxAccum = -10**9
            for dxAlpha, dyAlpha in dirAlpha:
                for dxBeta, dyBeta in dirBeta:
                    for dxGamma, dyGamma in dirGamma:
                        recurseResult = dp(a1 + dxAlpha, b1 + dyAlpha,
                                           a2 + dxBeta, b2 + dyBeta,
                                           a3 + dxGamma, b3 + dyGamma)
                        if recurseResult > maxAccum:
                            maxAccum = recurseResult

            memoMap[keyTuple] = collectedSum + maxAccum
            return collectedSum + maxAccum

        zeroVal = 0
        startX1, startY1 = zeroVal, zeroVal
        startX2, startY2 = zeroVal, nVar - 1
        startX3, startY3 = nVar - 1, zeroVal

        return dp(startX1, startY1, startX2, startY2, startX3, startY3)