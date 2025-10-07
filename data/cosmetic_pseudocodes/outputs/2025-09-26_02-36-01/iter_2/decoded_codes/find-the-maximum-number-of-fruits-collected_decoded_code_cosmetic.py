from math import inf
from functools import lru_cache

class Solution:
    def maxCollectedFruits(self, fruits):
        size = len(fruits)

        movementSet1 = [(1, 1), (0, 1)]
        movementSet2 = [(1, -1), (1, 0), (1, 1)]
        movementSet3 = [(-1, 1), (0, 1), (1, 1)]

        @lru_cache(None)
        def dp(aX, aY, bX, bY, cX, cY):
            # Check boundary conditions
            if (
                not (0 <= aX < size and 0 <= aY < size) or
                not (0 <= bX < size and 0 <= bY < size) or
                not (0 <= cX < size and 0 <= cY < size)
            ):
                return -inf

            finalPos = size - 1
            if aX == aY == bX == bY == cX == cY == finalPos:
                return fruits[finalPos][finalPos]

            key = (aX, aY, bX, bY, cX, cY)

            totalCollected = fruits[aY][aX]

            # If A overlaps with B or C, its fruits are only counted once, so zero here
            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                totalCollected = 0

            # If B and C overlap, add fruit only once
            if bX == cX and bY == cY:
                totalCollected += fruits[bY][bX]
            else:
                totalCollected += fruits[bY][bX] + fruits[cY][cX]

            bestGain = -inf
            for dx1, dy1 in movementSet1:
                for dx2, dy2 in movementSet2:
                    for dx3, dy3 in movementSet3:
                        trialVal = dp(aX + dx1, aY + dy1, bX + dx2, bY + dy2, cX + dx3, cY + dy3)
                        if trialVal > bestGain:
                            bestGain = trialVal

            resultValue = totalCollected + bestGain
            return resultValue

        return dp(0, 0, 0, size - 1, size - 1, 0)