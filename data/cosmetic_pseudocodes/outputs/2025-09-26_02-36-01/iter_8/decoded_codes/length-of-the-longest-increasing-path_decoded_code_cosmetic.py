from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        offsetToK = 0  # not used but preserved
        tempIndex = k
        baseTuple = coordinates[tempIndex]
        leftX, leftY = baseTuple[0], baseTuple[1]

        listAlpha = []
        iteratorI = 0
        while iteratorI < len(coordinates):
            currentPair = coordinates[iteratorI]
            alphaX, betaY = currentPair[0], currentPair[1]
            if not (alphaX >= leftX):
                if not (betaY >= leftY):
                    listAlpha.append((alphaX, betaY))
            iteratorI += 1

        listBeta = []
        indexN = 0
        while True:
            if indexN >= len(coordinates):
                break
            recordPair = coordinates[indexN]
            gammaX, deltaY = recordPair[0], recordPair[1]
            if gammaX > leftX:
                if deltaY > leftY:
                    listBeta.append((gammaX, deltaY))
            indexN += 1

        accumResult = 1
        recursiveLeft = self._lengthOfLIS(listAlpha)
        recursiveRight = self._lengthOfLIS(listBeta)
        summationTO = accumResult + recursiveLeft + recursiveRight
        return summationTO

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        def compareHelper(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
            if a[0] < b[0]:
                return True
            elif a[0] == b[0]:
                return a[1] > b[1]
            else:
                return False

        def customSort(arr: List[Tuple[int, int]]) -> None:
            length = len(arr)
            for indexOuter in range(length - 1):
                for indexInner in range(indexOuter + 1, length):
                    if compareHelper(arr[indexInner], arr[indexOuter]):
                        # swap arr[indexOuter] and arr[indexInner]
                        arr[indexOuter], arr[indexInner] = arr[indexInner], arr[indexOuter]

        customSort(coordinates)

        tailArray = []
        incrementerM = 0

        def bisectLeft(arr: List[int], target: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low

        while incrementerM < len(coordinates):
            currentElem = coordinates[incrementerM]
            # unusedVal = currentElem[0]  # unused in LIS calculation
            valueY = currentElem[1]

            if (len(tailArray) == 0) or (valueY > tailArray[-1]):
                tailArray.append(valueY)
            else:
                placePos = bisectLeft(tailArray, valueY)
                tailArray[placePos] = valueY
            incrementerM += 1

        return len(tailArray)