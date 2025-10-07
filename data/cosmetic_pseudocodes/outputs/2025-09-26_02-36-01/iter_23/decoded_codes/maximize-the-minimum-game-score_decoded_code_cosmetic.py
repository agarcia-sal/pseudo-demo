import math
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def isPossible(minVal: int, cutoffs: int) -> bool:
            def helper(index: int, accMoves: int, lastMoves: int) -> bool:
                if index == len(points):
                    return accMoves <= cutoffs
                needed = math.ceil((minVal + points[index] - 1) / points[index])
                currentReq = max(0, needed - lastMoves)
                if currentReq > 0:
                    newMovesAccum = accMoves + (2 * currentReq - 1)
                    newLastMoves = currentReq - 1
                    if newMovesAccum > cutoffs:
                        return False
                    return helper(index + 1, newMovesAccum, newLastMoves)
                else:
                    newMovesAccum = accMoves + 1
                    newLastMoves = 0 if index + 1 < len(points) else lastMoves
                    if newMovesAccum > cutoffs:
                        return False
                    return helper(index + 1, newMovesAccum, newLastMoves)
            return helper(0, 0, 0)

        def bisect(low: int, high: int) -> int:
            if low >= high:
                return low
            midVal = (low + high + 1) // 2
            if isPossible(midVal, m):
                return bisect(midVal, high)
            else:
                return bisect(low, midVal - 1)

        leftBorder = 0
        rightBorder = (((m + 1) // 2) * points[0])
        return bisect(leftBorder, rightBorder)