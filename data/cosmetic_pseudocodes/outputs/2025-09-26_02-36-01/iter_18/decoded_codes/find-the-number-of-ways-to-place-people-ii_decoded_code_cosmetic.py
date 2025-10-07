from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def sortPoints(arr: List[Point]) -> None:
            def swapElements(a: int, b: int) -> None:
                arr[a], arr[b] = arr[b], arr[a]

            m = len(arr)
            idx1 = 1
            while idx1 < m:
                idx2 = 0
                while idx2 < m - idx1:
                    if (arr[idx2].x > arr[idx2 + 1].x or
                        (arr[idx2].x == arr[idx2 + 1].x and arr[idx2].y < arr[idx2 + 1].y)):
                        swapElements(idx2, idx2 + 1)
                    idx2 += 1
                idx1 += 1

        sortPoints(points)

        total = len(points)
        sumPairs = 0

        def helperCheck(a: int, b: int) -> int:
            l = a + 1
            while l < b:
                px, py = points[l].x, points[l].y
                if (points[a].x <= px <= points[b].x and
                    points[b].y <= py <= points[a].y):
                    return 0
                l += 1
            return 1

        outerIdx = 0
        while outerIdx < total - 1:
            innerIdx = outerIdx + 1
            while innerIdx < total:
                firstX, firstY = points[outerIdx].x, points[outerIdx].y
                secondX, secondY = points[innerIdx].x, points[innerIdx].y

                if not (firstX > secondX or firstY < secondY):
                    if helperCheck(outerIdx, innerIdx) == 1:
                        sumPairs += 1
                innerIdx += 1
            outerIdx += 1

        return sumPairs