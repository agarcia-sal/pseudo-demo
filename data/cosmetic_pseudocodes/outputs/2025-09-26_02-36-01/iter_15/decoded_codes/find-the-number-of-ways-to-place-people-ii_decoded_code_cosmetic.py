from typing import List

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:

        def partition(arr: List[Point], left: int, right: int) -> int:
            pivotX = arr[right].x
            pivotY = arr[right].y
            index = left - 1
            for curr in range(left, right):
                cond1 = arr[curr].x <= pivotX
                cond2 = (arr[curr].x == pivotX)
                cond3 = arr[curr].y >= pivotY
                if cond1 and (not cond2 or cond3):
                    index += 1
                    arr[index], arr[curr] = arr[curr], arr[index]
            arr[index + 1], arr[right] = arr[right], arr[index + 1]
            return index + 1

        def quicksort(arr: List[Point], low: int, high: int) -> None:
            if low < high:
                pivotIndex = partition(arr, low, high)
                quicksort(arr, low, pivotIndex - 1)
                quicksort(arr, pivotIndex + 1, high)

        n = len(points)
        if n == 0:
            return 0

        quicksort(points, 0, n - 1)

        countPairs = 0

        for outerIndex in range(n - 1):
            px1 = points[outerIndex].x
            py1 = points[outerIndex].y
            for innerIndex in range(outerIndex + 1, n):
                px2 = points[innerIndex].x
                py2 = points[innerIndex].y

                if not (px1 > px2) and not (py1 < py2):
                    validFlag = True
                    for midIndex in range(outerIndex + 1, innerIndex):
                        pxk = points[midIndex].x
                        pyk = points[midIndex].y
                        condA = (px1 <= pxk)
                        condB = (pxk <= px2)
                        condC = (py2 <= pyk)
                        condD = (pyk <= py1)
                        if condA and condB and condC and condD:
                            validFlag = False
                            break
                    if validFlag:
                        countPairs += 1

        return countPairs