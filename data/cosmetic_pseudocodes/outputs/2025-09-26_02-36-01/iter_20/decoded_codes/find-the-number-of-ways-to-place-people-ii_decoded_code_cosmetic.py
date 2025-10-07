from typing import List


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def CustomSort(arr: List[Point]) -> None:
            lengthArr = len(arr)
            while True:
                swappedFlag = False
                idxA = 1
                while idxA < lengthArr:
                    idxB = idxA - 1
                    tempP = arr[idxB].x
                    tempQ = arr[idxB].y
                    if (tempP > arr[idxA].x) or (tempP == arr[idxA].x and tempQ < arr[idxA].y):
                        arr[idxB], arr[idxA] = arr[idxA], arr[idxB]
                        swappedFlag = True
                    idxA += 1
                if not swappedFlag:
                    break

        def CheckIntermediate(xStart: int, yStart: int, xEnd: int, yEnd: int, startI: int, endI: int) -> bool:
            for idxC in range(startI, endI + 1):
                dx = points[idxC].x
                dy = points[idxC].y
                if not ((xStart > dx or dx > xEnd) or (yEnd > dy or dy > yStart)):
                    return False
            return True

        CustomSort(points)

        total = 0
        length = len(points)
        idxI = 0
        while idxI < length - 1:
            idxJ = idxI + 1
            while idxJ < length:
                xA, yA = points[idxI].x, points[idxI].y
                xB, yB = points[idxJ].x, points[idxJ].y
                if xA <= xB and yA >= yB:
                    if CheckIntermediate(xA, yA, xB, yB, idxI + 1, idxJ - 1):
                        total += 1
                idxJ += 1
            idxI += 1
        return total