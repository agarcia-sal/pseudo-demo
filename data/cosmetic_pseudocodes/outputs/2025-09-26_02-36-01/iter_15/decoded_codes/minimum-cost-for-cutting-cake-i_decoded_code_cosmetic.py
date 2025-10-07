from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def reverseSortDescending(arr: List[int]) -> None:
            arr.sort()
            startIdx, endIdx = 0, len(arr) - 1
            while startIdx < endIdx:
                arr[startIdx], arr[endIdx] = arr[endIdx], arr[startIdx]
                startIdx += 1
                endIdx -= 1

        reverseSortDescending(horizontalCut)
        reverseSortDescending(verticalCut)

        accumulatedCost = 0
        idxHorizontal = 0
        idxVertical = 0

        multiplierHorizontal = 1
        multiplierVertical = 1

        def loopCondition(x: int, y: int, p: int, q: int) -> bool:
            return (x < p - 1) or (y < q - 1)

        while loopCondition(idxHorizontal, idxVertical, m, n):
            if (idxVertical == n - 1) or ((idxHorizontal < m - 1) and (horizontalCut[idxHorizontal] > verticalCut[idxVertical])):
                addCost = horizontalCut[idxHorizontal] * multiplierVertical
                accumulatedCost += addCost
                multiplierHorizontal += 1
                idxHorizontal += 1
            else:
                addCost = verticalCut[idxVertical] * multiplierHorizontal
                accumulatedCost += addCost
                multiplierVertical += 1
                idxVertical += 1

        return accumulatedCost