from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort arr in descending order using a custom quicksort implementation
        def sortDescending(arr: List[int]) -> None:
            def recurseSort(startIndex: int, endIndex: int) -> None:
                if startIndex >= endIndex:
                    return
                pivotIndex = startIndex
                leftCursor = startIndex + 1
                rightCursor = endIndex
                while leftCursor <= rightCursor:
                    if arr[leftCursor] >= arr[pivotIndex]:
                        leftCursor += 1
                    elif arr[rightCursor] < arr[pivotIndex]:
                        rightCursor -= 1
                    else:
                        arr[leftCursor], arr[rightCursor] = arr[rightCursor], arr[leftCursor]
                        leftCursor += 1
                        rightCursor -= 1
                arr[pivotIndex], arr[rightCursor] = arr[rightCursor], arr[pivotIndex]
                recurseSort(startIndex, rightCursor - 1)
                recurseSort(rightCursor + 1, endIndex)
            recurseSort(0, len(arr) - 1)

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        accumulator = 0
        idxA = 0
        idxB = 0
        countH = 1
        countV = 1

        def loopProcess(indexA: int, indexB: int, acc: int, countHorizontal: int, countVertical: int) -> int:
            if indexA >= len(horizontalCut) and indexB >= len(verticalCut):
                return acc
            if (indexB >= len(verticalCut)) or (indexA < len(horizontalCut) and horizontalCut[indexA] > verticalCut[indexB]):
                partialSum = acc + horizontalCut[indexA] * countVertical
                return loopProcess(indexA + 1, indexB, partialSum, countHorizontal + 1, countVertical)
            else:
                partialSum = acc + verticalCut[indexB] * countHorizontal
                return loopProcess(indexA, indexB + 1, partialSum, countHorizontal, countVertical + 1)

        return loopProcess(idxA, idxB, accumulator, countH, countV)