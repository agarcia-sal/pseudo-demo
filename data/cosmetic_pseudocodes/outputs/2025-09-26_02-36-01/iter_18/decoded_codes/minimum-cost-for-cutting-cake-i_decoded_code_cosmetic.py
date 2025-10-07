from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:

        def sortDescending(arr: List[int]) -> None:
            # Bubble sort descending as per pseudocode
            while True:
                swapped = False
                for pos in range(len(arr) - 1):
                    if arr[pos] < arr[pos + 1]:
                        arr[pos], arr[pos + 1] = arr[pos + 1], arr[pos]
                        swapped = True
                if not swapped:
                    break

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        totalResult = 0
        idxH = 0
        idxV = 0
        countH = 1
        countV = 1

        def conditionMet() -> bool:
            return (idxV == n - 1) or (idxH < m - 1 and horizontalCut[idxH] > verticalCut[idxV])

        while idxH < m -1 or idxV < n -1:
            if conditionMet():
                stepValue = horizontalCut[idxH] * countV
                totalResult += stepValue
                countH += 1
                idxH += 1
            else:
                stepValue = verticalCut[idxV] * countH
                totalResult += stepValue
                countV += 1
                idxV += 1

        return totalResult