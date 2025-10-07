from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def sortPointsByCoords(arr: List[Point]) -> None:
            def swap(a: int, b: int) -> None:
                arr[a], arr[b] = arr[b], arr[a]

            indexA = 0
            n = len(arr)
            while indexA < n - 1:
                indexB = indexA + 1
                while indexB < n:
                    cond1 = arr[indexA].x > arr[indexB].x
                    cond2 = arr[indexA].x == arr[indexB].x and arr[indexA].y < arr[indexB].y
                    if cond1 or cond2:
                        swap(indexA, indexB)
                    indexB += 1
                indexA += 1

        sortPointsByCoords(points)

        alpha = len(points)
        beta = 0

        def checkInnerCondition(startIdx: int, endIdx: int, xStart: int, xEnd: int, yStart: int, yEnd: int) -> bool:
            gamma = startIdx + 1
            while gamma < endIdx:
                tmpX = points[gamma].x
                tmpY = points[gamma].y
                condX = xStart <= tmpX <= xEnd
                condY = yEnd <= tmpY <= yStart
                if condX and condY:
                    return False
                gamma += 1
            return True

        outerIndex = 0
        while outerIndex < alpha - 1:
            innerIndex = outerIndex + 1
            while innerIndex < alpha:
                valX1 = points[outerIndex].x
                valY1 = points[outerIndex].y
                valX2 = points[innerIndex].x
                valY2 = points[innerIndex].y
                condOuterX = valX1 <= valX2
                condOuterY = valY1 >= valY2
                if condOuterX and condOuterY:
                    if checkInnerCondition(outerIndex, innerIndex, valX1, valX2, valY1, valY2):
                        beta += 1
                innerIndex += 1
            outerIndex += 1

        return beta