from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDescending(arr: List[int]) -> None:
            def swapElements(x: int, y: int) -> None:
                arr[x], arr[y] = arr[y], arr[x]

            outerIndex = 0
            length = len(arr)
            while outerIndex < length:
                madeSwap = False
                innerIndex = 0
                while innerIndex < length - 1:
                    if arr[innerIndex] < arr[innerIndex + 1]:
                        swapElements(innerIndex, innerIndex + 1)
                        madeSwap = True
                    innerIndex += 1
                if not madeSwap:
                    break
                outerIndex += 1

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        totalCost = 0
        indexH = 0
        indexV = 0
        countH = 1
        countV = 1

        def shouldContinue(x: int, y: int) -> bool:
            return (x < m - 1) or (y < n - 1)

        def isCHGreater(indexX: int, indexY: int) -> bool:
            return horizontalCut[indexX] > verticalCut[indexY]

        while shouldContinue(indexH, indexV):
            if (indexV == n - 1) or ((indexH < m - 1) and isCHGreater(indexH, indexV)):
                totalCost += horizontalCut[indexH] * countV
                countH += 1
                indexH += 1
            else:
                totalCost += verticalCut[indexV] * countH
                countV += 1
                indexV += 1

        return totalCost