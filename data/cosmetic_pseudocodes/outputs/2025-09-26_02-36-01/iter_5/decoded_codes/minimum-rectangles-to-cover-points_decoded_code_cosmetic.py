from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, coords: List[Tuple[int, int]], width: int) -> int:
        def sortPoints(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            if len(arr) < 2:
                return arr
            midIndex = len(arr) // 2
            leftPart = sortPoints(arr[:midIndex])
            rightPart = sortPoints(arr[midIndex:])
            return mergeSorted(leftPart, rightPart)

        def mergeSorted(leftArr: List[Tuple[int, int]], rightArr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            mergedResult = []
            leftIdx = 0
            rightIdx = 0
            while leftIdx < len(leftArr) and rightIdx < len(rightArr):
                if leftArr[leftIdx][0] <= rightArr[rightIdx][0]:
                    mergedResult.append(leftArr[leftIdx])
                    leftIdx += 1
                else:
                    mergedResult.append(rightArr[rightIdx])
                    rightIdx += 1
            while leftIdx < len(leftArr):
                mergedResult.append(leftArr[leftIdx])
                leftIdx += 1
            while rightIdx < len(rightArr):
                mergedResult.append(rightArr[rightIdx])
                rightIdx += 1
            return mergedResult

        sortedCoords = sortPoints(coords)
        totalRectangles = 0
        limitX = -1

        def processPoints(index: int, limitXVal: int, rectCount: int) -> int:
            if index == len(sortedCoords):
                return rectCount
            ptX, ptY = sortedCoords[index]
            updatedLimitX = limitXVal
            updatedRectCount = rectCount
            if ptX > updatedLimitX:
                updatedLimitX = ptX + width
                updatedRectCount += 1
            return processPoints(index + 1, updatedLimitX, updatedRectCount)

        return processPoints(0, limitX, totalRectangles)