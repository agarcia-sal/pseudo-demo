from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        def sortKey(point: Point):
            return (point.x, -point.y)

        points.sort(key=sortKey)

        lengthPoints = len(points)
        pairCount = 0

        def innerLoop(startI: int, startJ: int, isValidFlag: bool) -> bool:
            if startJ > startI + 1:
                currentPoint = points[startJ - 1]
                xkLocal = currentPoint.x
                ykLocal = currentPoint.y

                if not (xkLocal < points[startI].x or xkLocal > points[startJ].x
                        or ykLocal < points[startJ].y or ykLocal > points[startI].y):
                    isValidFlag = False

                return innerLoop(startI, startJ - 1, isValidFlag)
            else:
                return isValidFlag

        def outerLoop(iLocal: int):
            nonlocal pairCount
            if iLocal >= lengthPoints - 1:
                return
            jLocal = iLocal + 1
            while jLocal < lengthPoints:
                pI = points[iLocal]
                pJ = points[jLocal]

                if pI.x <= pJ.x and pI.y >= pJ.y:
                    defValid = innerLoop(iLocal, jLocal, True)
                    if defValid:
                        pairCount += 1
                jLocal += 1
            outerLoop(iLocal + 1)

        outerLoop(0)

        return pairCount