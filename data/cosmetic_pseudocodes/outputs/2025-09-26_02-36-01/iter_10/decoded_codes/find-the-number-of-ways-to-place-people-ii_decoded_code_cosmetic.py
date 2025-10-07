from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def comparePoints(a: Point, b: Point) -> int:
            if a.x > b.x or (a.x == b.x and a.y < b.y):
                return 1
            elif a.x == b.x and a.y == b.y:
                return 0
            else:
                return -1

        def reorder(arr: List[Point], startIndex: int, endIndex: int) -> None:
            if startIndex >= endIndex:
                return
            pivotVal = arr[endIndex]
            leftPtr = startIndex
            for tmpPtr in range(startIndex, endIndex):
                if comparePoints(arr[tmpPtr], pivotVal) <= 0:
                    arr[leftPtr], arr[tmpPtr] = arr[tmpPtr], arr[leftPtr]
                    leftPtr += 1
            arr[leftPtr], arr[endIndex] = arr[endIndex], arr[leftPtr]
            reorder(arr, startIndex, leftPtr - 1)
            reorder(arr, leftPtr + 1, endIndex)

        reorder(points, 0, len(points) - 1)

        totalElements = len(points)
        totalCount = 0

        def checkInnerRange(startIndex: int, endIndex: int, xStart: int, yStart: int, xEnd: int, yEnd: int) -> bool:
            if startIndex >= endIndex:
                return True
            scanIndex = startIndex
            while scanIndex < endIndex:
                p = points[scanIndex]
                if xStart <= p.x <= xEnd and yEnd <= p.y <= yStart:
                    return False
                scanIndex += 1
            return True

        def iterateInnerBlocks(idx: int) -> None:
            nonlocal totalCount
            if idx >= totalElements - 1:
                return
            inner = idx + 1
            while inner < totalElements:
                firstX, firstY = points[idx].x, points[idx].y
                secondX, secondY = points[inner].x, points[inner].y

                if firstX <= secondX and firstY >= secondY:
                    if checkInnerRange(idx + 1, inner, firstX, firstY, secondX, secondY):
                        totalCount += 1

                inner += 1
            iterateInnerBlocks(idx + 1)

        iterateInnerBlocks(0)
        return totalCount