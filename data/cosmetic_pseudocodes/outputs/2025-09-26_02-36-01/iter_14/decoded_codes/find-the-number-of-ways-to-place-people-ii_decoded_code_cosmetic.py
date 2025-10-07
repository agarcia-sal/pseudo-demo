from typing import List


class Point:
    __slots__ = ['x', 'y']

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:

        def swapIfNeeded(a: List[Point], idxA: int, b: List[Point], idxB: int):
            if a[idxA].x > b[idxB].x:
                a[idxA], b[idxB] = b[idxB], a[idxA]

        def customSort(arr: List[Point]):
            lenArr = len(arr)
            while True:
                changedFlag = False
                pos = 0
                while pos < lenArr - 1:
                    px, py = arr[pos].x, arr[pos].y
                    nx, ny = arr[pos + 1].x, arr[pos + 1].y
                    if px > nx or (px == nx and py < ny):
                        arr[pos], arr[pos + 1] = arr[pos + 1], arr[pos]
                        changedFlag = True
                    pos += 1
                if not changedFlag:
                    break

        customSort(points)

        totalPoints = len(points)

        def checkValidRange(startIdx: int, endIdx: int) -> bool:
            def insideBounds(xBound1, xMid, xBound2, yBound1, yMid, yBound2) -> bool:
                return (xBound1 <= xMid <= xBound2) and (yBound2 <= yMid <= yBound1)

            def innerLoop(indexStart: int, indexEnd: int) -> bool:
                if indexStart > indexEnd:
                    return True
                px, py = points[indexStart].x, points[indexStart].y
                refX1, refY1 = points[startIdx].x, points[startIdx].y
                refX2, refY2 = points[endIdx].x, points[endIdx].y
                if insideBounds(refX1, px, refX2, refY1, py, refY2):
                    return False
                return innerLoop(indexStart + 1, indexEnd)

            return innerLoop(startIdx + 1, endIdx - 1)

        def recursiveOuter(currentIndex: int) -> int:
            if currentIndex >= totalPoints - 1:
                return 0

            def recursiveInner(innerIndex: int) -> int:
                if innerIndex > totalPoints - 1:
                    return 0
                startX, startY = points[currentIndex].x, points[currentIndex].y
                innerX, innerY = points[innerIndex].x, points[innerIndex].y
                accumCount = 0
                if startX <= innerX and startY >= innerY:
                    if checkValidRange(currentIndex, innerIndex):
                        accumCount = 1
                return accumCount + recursiveInner(innerIndex + 1)

            return recursiveInner(currentIndex + 1) + recursiveOuter(currentIndex + 1)

        totalCount = recursiveOuter(0)
        return totalCount