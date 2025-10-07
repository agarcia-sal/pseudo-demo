from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        self.sortPoints(points, 0, len(points) - 1)
        totalPairs = 0
        idx1 = 0
        while idx1 <= len(points) - 2:
            idx2 = idx1 + 1
            while idx2 <= len(points) - 1:
                if self.compareCoords(points[idx1].x, points[idx2].x, points[idx1].y, points[idx2].y):
                    isValid = self.checkIntermediate(points, idx1, idx2)
                    if isValid:
                        totalPairs += 1
                idx2 += 1
            idx1 += 1
        return totalPairs

    def compareCoords(self, xa: int, xb: int, ya: int, yb: int) -> bool:
        return (not (xa > xb)) and (not (ya < yb))

    def checkIntermediate(self, arr: List[Point], posStart: int, posEnd: int) -> bool:
        validFlag = True
        posCurrent = posStart + 1
        startX, startY = arr[posStart].x, arr[posStart].y
        endX, endY = arr[posEnd].x, arr[posEnd].y
        while posCurrent <= posEnd - 1:
            currX, currY = arr[posCurrent].x, arr[posCurrent].y
            if (startX <= currX <= endX) and (endY <= currY <= startY):
                validFlag = False
                break
            posCurrent += 1
        return validFlag

    def sortPoints(self, arr: List[Point], left: int, right: int) -> None:
        if left >= right:
            return
        pivotIndex = self.partition(arr, left, right)
        self.sortPoints(arr, left, pivotIndex - 1)
        self.sortPoints(arr, pivotIndex + 1, right)

    def partition(self, arr: List[Point], low: int, high: int) -> int:
        pivotX = arr[high].x
        pivotY = arr[high].y
        i = low - 1
        for j in range(low, high):
            if (arr[j].x < pivotX) or (arr[j].x == pivotX and arr[j].y > pivotY):
                i += 1
                self.swap(arr, i, j)
        self.swap(arr, i + 1, high)
        return i + 1

    def swap(self, arr: List[Point], idxA: int, idxB: int) -> None:
        arr[idxA].x, arr[idxB].x = arr[idxB].x, arr[idxA].x
        arr[idxA].y, arr[idxB].y = arr[idxB].y, arr[idxA].y