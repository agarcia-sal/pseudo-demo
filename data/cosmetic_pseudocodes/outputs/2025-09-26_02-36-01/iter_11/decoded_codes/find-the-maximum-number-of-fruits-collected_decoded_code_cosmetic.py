from math import inf

class Solution:
    def maxCollectedFruits(self, fruits):
        totalLen = len(fruits)

        movesA = [(1, 1), (1, 0)]
        movesB = [(1, -1), (1, 0), (1, 1)]
        movesC = [(-1, 1), (0, 1), (1, 1)]

        cache = {}

        def dp(aX, aY, bX, bY, cX, cY):
            # Boundary checks
            if not (0 <= aX < totalLen and 0 <= aY < totalLen):
                return -inf
            if not (0 <= bX < totalLen and 0 <= bY < totalLen):
                return -inf
            if not (0 <= cX < totalLen and 0 <= cY < totalLen):
                return -inf

            finalPos = totalLen - 1
            if aX == aY == bX == bY == cX == cY == finalPos:
                return fruits[finalPos][finalPos]

            keyTuple = (aX, aY, bX, bY, cX, cY)
            if keyTuple in cache:
                return cache[keyTuple]

            fruitSum = fruits[aX][aY]
            # If A overlaps with either B or C's position, zero out this fruit sum since already accounted elsewhere
            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                fruitSum = 0

            # For B and C positions, if they are the same cell, add fruit once; otherwise add both
            if bX == cX and bY == cY:
                fruitSum += fruits[bX][bY]
            else:
                fruitSum += fruits[bX][bY] + fruits[cX][cY]

            def recurseIter(d1, i1):
                if i1 >= len(d1):
                    return -inf
                dx1, dy1 = d1[i1]

                def recurseJ(d2, i2):
                    if i2 >= len(d2):
                        return -inf
                    dx2, dy2 = d2[i2]

                    def recurseK(d3, i3, bestSoFar):
                        if i3 >= len(d3):
                            return bestSoFar
                        dx3, dy3 = d3[i3]
                        cand = dp(aX + dx1, aY + dy1, bX + dx2, bY + dy2, cX + dx3, cY + dy3)
                        if cand > bestSoFar:
                            bestSoFar = cand
                        return recurseK(d3, i3 + 1, bestSoFar)

                    return recurseK(movesC, 0, -inf)

                innerBest = recurseJ(movesB, 0)
                restBest = recurseIter(d1, i1 + 1)
                return innerBest if innerBest > restBest else restBest

            maxVal = recurseIter(movesA, 0)

            resultVal = fruitSum + maxVal
            cache[keyTuple] = resultVal
            return resultVal

        return dp(0, 0, 0, totalLen - 1, totalLen - 1, 0)