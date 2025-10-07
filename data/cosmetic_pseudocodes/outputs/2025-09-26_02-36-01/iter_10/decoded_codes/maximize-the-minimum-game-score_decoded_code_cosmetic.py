import math
from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:
        def isPossible(minVal: int, m: int) -> bool:
            moveCounter = 0
            priorMove = 0
            idx = 0
            n = len(points)
            while idx < n:
                pt = points[idx]
                neededSegment = math.ceil((minVal + pt - 1) / pt)
                if (neededSegment - priorMove) < 0:
                    neededSegment = 0
                else:
                    neededSegment = neededSegment - priorMove
                if neededSegment > 0:
                    moveCounter += 2 * neededSegment - 1
                    priorMove = neededSegment - 1
                elif idx + 1 < n:
                    moveCounter += 1
                    priorMove = 0
                if moveCounter > m:
                    return False
                idx += 1
            return True

        leftBound = 0
        rightBound = ((m + 1) // 2) * (points[0] + 1)

        def binarySearch() -> None:
            nonlocal leftBound, rightBound
            if leftBound >= rightBound:
                return
            midpoint = (leftBound + rightBound + 1) // 2
            if isPossible(midpoint, m):
                leftBound = midpoint
            else:
                rightBound = midpoint - 1
            binarySearch()

        binarySearch()
        return leftBound