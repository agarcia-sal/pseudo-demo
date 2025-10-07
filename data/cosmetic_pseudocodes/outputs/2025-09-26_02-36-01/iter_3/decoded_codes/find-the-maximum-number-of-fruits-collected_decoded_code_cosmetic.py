from math import inf
from functools import lru_cache
from typing import List

class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        size = len(fruits)
        movesA = [(1, 1), (0, 1)]
        movesB = [(1, -1), (1, 0), (1, 1)]
        movesC = [(-1, 1), (0, 1), (1, 1)]

        @lru_cache(None)
        def dp(aX: int, aY: int, bX: int, bY: int, cX: int, cY: int) -> int:
            # Boundary checks
            if not (0 <= aX < size and 0 <= aY < size):
                return -inf
            if not (0 <= bX < size and 0 <= bY < size):
                return -inf
            if not (0 <= cX < size and 0 <= cY < size):
                return -inf

            # All three at bottom-right corner (goal)
            if (aX == aY == bX == bY == cX == cY == size - 1):
                return fruits[size - 1][size - 1]

            gathered = fruits[aX][aY]
            if (aX == bX and aY == bY) or (aX == cX and aY == cY):
                gathered = 0

            if bX == cX and bY == cY:
                gathered += fruits[bX][bY]
            else:
                gathered += fruits[bX][bY] + fruits[cX][cY]

            best = -inf
            for stepA in movesA:
                newA_X = aX + stepA[0]
                newA_Y = aY + stepA[1]
                for stepB in movesB:
                    newB_X = bX + stepB[0]
                    newB_Y = bY + stepB[1]
                    for stepC in movesC:
                        newC_X = cX + stepC[0]
                        newC_Y = cY + stepC[1]

                        result = dp(newA_X, newA_Y, newB_X, newB_Y, newC_X, newC_Y)
                        if result > best:
                            best = result

            return gathered + best

        return dp(0, 0, 0, size - 1, size - 1, 0)