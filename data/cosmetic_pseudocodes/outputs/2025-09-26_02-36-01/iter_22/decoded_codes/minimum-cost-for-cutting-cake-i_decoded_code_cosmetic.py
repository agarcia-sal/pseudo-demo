from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # SortDescending using Python's built-in sort for efficiency and correctness
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        totalCost = 0
        idxH = 0
        idxV = 0
        countH = 1
        countV = 1

        def ConditionA() -> bool:
            return (idxV == n - 1) or ((idxH < m - 1) and (horizontalCut[idxH] > verticalCut[idxV]))

        while not (idxH >= m - 1 and idxV >= n - 1):
            if ConditionA():
                totalCost += horizontalCut[idxH] * countV
                countH += 1
                idxH += 1
            else:
                totalCost += verticalCut[idxV] * countH
                countV += 1
                idxV += 1

        return totalCost