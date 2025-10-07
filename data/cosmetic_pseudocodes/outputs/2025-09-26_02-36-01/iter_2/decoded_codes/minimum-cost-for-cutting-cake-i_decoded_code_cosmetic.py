from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        totalCost = 0
        idxH, idxV = 0, 0
        countH, countV = 1, 1

        while idxH < m - 1 or idxV < n - 1:
            if idxV == n - 1 or (idxH < m - 1 and horizontalCut[idxH] > verticalCut[idxV]):
                totalCost += horizontalCut[idxH] * countV
                countH += 1
                idxH += 1
            else:
                totalCost += verticalCut[idxV] * countH
                countV += 1
                idxV += 1

        return totalCost