from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        def customSort(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            # Simple bubble sort based on x-coordinate
            n = len(arr)
            i = 0
            while i < n - 1:
                j = i + 1
                while j < n:
                    if arr[j][0] < arr[i][0]:
                        arr[i], arr[j] = arr[j], arr[i]
                    j += 1
                i += 1
            return arr

        sortedPoints = customSort(points)
        rectanglesCount = 0
        coverageLimit = 0

        def isGreater(a: int, b: int) -> bool:
            return a > b

        def incrementCounter(val: int) -> int:
            return val + 1

        index = 0
        total = len(sortedPoints)
        while index < total:
            pointX = sortedPoints[index][0]
            if isGreater(pointX, coverageLimit):
                coverageLimit = pointX + w
                rectanglesCount = incrementCounter(rectanglesCount)
            index += 1

        return rectanglesCount