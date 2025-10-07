from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        def sortPointsByX(inputList: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(inputList) <= 1:
                return inputList
            pivotIndex = len(inputList) // 2
            pivotValue = inputList[pivotIndex][0]
            leftPartition = []
            rightPartition = []
            for i, point in enumerate(inputList):
                if i != pivotIndex:
                    if point[0] <= pivotValue:
                        leftPartition.append(point)
                    else:
                        rightPartition.append(point)
            return sortPointsByX(leftPartition) + [inputList[pivotIndex]] + sortPointsByX(rightPartition)

        sortedList = sortPointsByX(points)
        rectCount = 0
        boundaryLimit = -1
        iterator = 0
        while iterator < len(sortedList):
            pointX = sortedList[iterator][0]
            if boundaryLimit < pointX:
                boundaryLimit = pointX + w
                rectCount += 1
            iterator += 1
        return rectCount