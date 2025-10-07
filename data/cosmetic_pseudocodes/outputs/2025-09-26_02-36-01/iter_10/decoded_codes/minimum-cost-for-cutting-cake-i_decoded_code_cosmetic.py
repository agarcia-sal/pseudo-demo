from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def descSort(arr: List[int]) -> None:
            # Insertion sort arr in descending order
            for idx in range(1, len(arr)):
                tempPos = idx
                while tempPos > 0 and arr[tempPos] > arr[tempPos - 1]:
                    arr[tempPos], arr[tempPos - 1] = arr[tempPos - 1], arr[tempPos]
                    tempPos -= 1

        descSort(horizontalCut)
        descSort(verticalCut)

        totalCost = 0
        horizIdx = 0
        vertIdx = 0
        horizSeg = 1
        vertSeg = 1

        def recursiveProcess(a: int, b: int, x: int, y: int) -> None:
            nonlocal totalCost, horizSeg, vertSeg
            if not (a < m - 1 or b < n - 1):
                return
            else:
                if b == n - 1 or (a < m - 1 and horizontalCut[a] > verticalCut[b]):
                    totalCost += horizontalCut[a] * vertSeg
                    horizSeg += 1
                    recursiveProcess(a + 1, b, x, y)
                else:
                    totalCost += verticalCut[b] * horizSeg
                    vertSeg += 1
                    recursiveProcess(a, b + 1, x, y)

        recursiveProcess(horizIdx, vertIdx, horizSeg, vertSeg)

        return totalCost