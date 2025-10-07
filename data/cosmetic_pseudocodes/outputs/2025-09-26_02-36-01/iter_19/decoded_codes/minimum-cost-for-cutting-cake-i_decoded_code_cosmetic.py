from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def sortDescending(arr: List[int]) -> None:
            size = len(arr)
            for idx in range(size - 1):
                for pos in range(size - idx - 1):
                    if arr[pos] < arr[pos + 1]:
                        arr[pos], arr[pos + 1] = arr[pos + 1], arr[pos]

        sortDescending(horizontalCut)
        sortDescending(verticalCut)

        aggregate = 0
        firstIndex = 0
        secondIndex = 0
        firstCount = 1
        secondCount = 1

        while not (firstIndex >= m - 1 and secondIndex >= n - 1):
            if secondIndex == n - 1:
                aggregate += horizontalCut[firstIndex] * secondCount
                firstCount += 1
                firstIndex += 1
            elif firstIndex < m - 1 and horizontalCut[firstIndex] > verticalCut[secondIndex]:
                aggregate += horizontalCut[firstIndex] * secondCount
                firstCount += 1
                firstIndex += 1
            else:
                aggregate += verticalCut[secondIndex] * firstCount
                secondCount += 1
                secondIndex += 1

        return aggregate