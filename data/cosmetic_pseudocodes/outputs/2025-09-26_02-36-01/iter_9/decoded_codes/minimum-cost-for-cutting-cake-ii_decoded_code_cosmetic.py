from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDescending(arr: List[int]) -> None:
            for p in range(1, len(arr)):
                q = p
                while q > 0 and arr[q] > arr[q - 1]:
                    arr[q], arr[q - 1] = arr[q - 1], arr[q]
                    q -= 1

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        totalCost = 0
        idxH = 0
        idxV = 0
        heightCount = 1
        widthCount = 1

        def hasMoreCuts(x: int, y: int) -> bool:
            return x < y

        while hasMoreCuts(idxH, len(horizontalCut)) or hasMoreCuts(idxV, len(verticalCut)):
            if idxV == len(verticalCut) or (idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]):
                addVal = horizontalCut[idxH] * widthCount
                totalCost += addVal
                heightCount += 1
                idxH += 1
            else:
                addVal = verticalCut[idxV] * heightCount
                totalCost += addVal
                widthCount += 1
                idxV += 1

        return totalCost