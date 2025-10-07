class Solution:
    def maxCollectedFruits(self, fruits):
        lengthVar = len(fruits)

        movesA = [(1, 0), (1, 1)]
        movesB = [(1, -1), (1, 0), (0, 1)]
        movesC = [(0, -1), (-1, 1), (1, 1)]

        cacheMap = {}

        def recursiveSearch(aX, aY, bX, bY, cX, cY):
            # Check out-of-bound indices
            if (
                aX < 0 or aX >= lengthVar or aY < 0 or aY >= lengthVar or
                bX < 0 or bX >= lengthVar or bY < 0 or bY >= lengthVar or
                cX < 0 or cX >= lengthVar or cY < 0 or cY >= lengthVar
            ):
                return float('-inf')

            # Terminal condition: all points meet at (lengthVar - 1, lengthVar - 1)
            if (
                aX == aY == bX == bY == cX == cY == (lengthVar - 1)
            ):
                return fruits[lengthVar - 1][lengthVar - 1]

            key = (aX, aY, bX, bY, cX, cY)
            if key in cacheMap:
                return cacheMap[key]

            sumVar = fruits[aY][aX]

            # If a and b occupy the same cell or a and c occupy the same cell, reset sumVar to 0
            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                sumVar = 0

            if bX == cX and bY == cY:
                sumVar += fruits[bY][bX]
            else:
                sumVar += fruits[bY][bX] + fruits[cY][cX]

            maxResult = float('-inf')

            for dxA, dyA in movesA:
                for dxB, dyB in movesB:
                    for dxC, dyC in movesC:
                        tempCandidate = recursiveSearch(
                            aX + dxA, aY + dyA,
                            bX + dxB, bY + dyB,
                            cX + dxC, cY + dyC,
                        )
                        if tempCandidate > maxResult:
                            maxResult = tempCandidate

            cacheMap[key] = sumVar + maxResult
            return sumVar + maxResult

        return recursiveSearch(0, 0, 0, lengthVar - 1, lengthVar - 1, 0)