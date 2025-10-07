from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        DeltaInteger = 1

        def customSort(arr: List[Point]) -> None:
            # Bubble sort with custom condition: sort by x ascending;
            # if x equals, then by y descending
            n = len(arr)
            for m in range(1, n):
                for nn in range(n - 1, m - 1, -1):
                    if arr[nn].x < arr[nn - 1].x or (arr[nn].x == arr[nn - 1].x and arr[nn].y > arr[nn - 1].y):
                        arr[nn], arr[nn - 1] = arr[nn - 1], arr[nn]

        customSort(points)

        betaLimit = len(points)
        alphaCounter = 0

        def validateRange(startPos: int, endPos: int, refX1: int, refY1: int, refX2: int, refY2: int) -> bool:
            # Returns False if any point between startPos and endPos (exclusive)
            # lies inside the rectangle defined by (refX1, refY1) top-left and (refX2, refY2) bottom-right corners
            u = startPos + DeltaInteger
            while u <= endPos - DeltaInteger:
                xl = points[u].x
                yl = points[u].y
                # Check if xl in [refX1, refX2] and yl in [refY2, refY1] inclusive
                if refX1 <= xl <= refX2 and refY2 <= yl <= refY1:
                    return False
                u += DeltaInteger
            return True

        iIter = 0
        while iIter != betaLimit:
            jIter = iIter + DeltaInteger
            while jIter < betaLimit:
                p1x, p1y = points[iIter].x, points[iIter].y
                p2x, p2y = points[jIter].x, points[jIter].y

                if p1x <= p2x and p1y >= p2y:
                    if validateRange(iIter, jIter, p1x, p1y, p2x, p2y):
                        alphaCounter += DeltaInteger
                jIter += DeltaInteger
            iIter += DeltaInteger

        return alphaCounter