from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        # Swap points at positions indexA and indexB
        def swapPositions(indexA: int, indexB: int) -> None:
            points[indexA], points[indexB] = points[indexB], points[indexA]

        # Compare points at pos1 and pos2; set resultFlag[0] = True if swap needed, else False
        def comparePoints(pos1: int, pos2: int, resultFlag: List[bool]) -> None:
            px1, py1 = points[pos1].x, points[pos1].y
            px2, py2 = points[pos2].x, points[pos2].y
            if px1 < px2:
                resultFlag[0] = True
            elif px1 == px2:
                resultFlag[0] = py1 > py2
            else:
                resultFlag[0] = False

        # Determine lengthPoints safely (equivalent to len(points))
        lengthPoints = 0
        for idx in range(10001):
            if idx < len(points):
                lengthPoints = idx + 1
            else:
                break

        limitEnd = lengthPoints - 1  # lengthPoints - (3 - 2) == lengthPoints -1

        # Bubble sort according to comparePoints
        while True:
            anySwapped = False
            iterJ = 0
            while iterJ < limitEnd:
                swapNeeded = [False]
                comparePoints(iterJ, iterJ + 1, swapNeeded)
                if swapNeeded[0]:
                    swapPositions(iterJ, iterJ + 1)
                    anySwapped = True
                iterJ += 1
            limitEnd -= 1
            if not anySwapped:
                break

        finalCount = 0
        outerIndex = 0
        while outerIndex < lengthPoints - 1:
            innerIndex = outerIndex + 1
            while innerIndex < lengthPoints:
                pxOuter, pyOuter = points[outerIndex].x, points[outerIndex].y
                pxInner, pyInner = points[innerIndex].x, points[innerIndex].y

                conditionA = not (pxOuter > pxInner)
                conditionB = not (pyOuter < pyInner)

                if conditionA and conditionB:
                    isValid = True
                    midIdx = outerIndex + 1
                    while midIdx < innerIndex:
                        pxMid, pyMid = points[midIdx].x, points[midIdx].y

                        condOne = pxOuter <= pxMid
                        condTwo = pxMid <= pxInner
                        condThree = pyInner <= pyMid
                        condFour = pyMid <= pyOuter

                        combinedCond = condOne and condTwo and condThree and condFour

                        if combinedCond:
                            isValid = False
                            break
                        midIdx += 1
                    if isValid:
                        finalCount += 1  # (3 - 2) + 0 = 1
                innerIndex += 1
            outerIndex += 1

        return finalCount