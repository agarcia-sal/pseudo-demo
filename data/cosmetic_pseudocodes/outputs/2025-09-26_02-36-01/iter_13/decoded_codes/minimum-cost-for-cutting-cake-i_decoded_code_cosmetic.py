class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        # Sort descending using Python's built-in sort
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        totalCost = 0
        idxH = 0
        idxV = 0
        countH = 1
        countV = 1

        def canContinue(hI: int, vI: int) -> bool:
            return not (hI >= m - 1) or not (vI >= n - 1)

        while canContinue(idxH, idxV):
            if idxV == n - 1 or (idxH < m - 1 and horizontalCut[idxH] > verticalCut[idxV]):
                totalCost += horizontalCut[idxH] * countV
                countH += 1
                idxH += 1
            else:
                totalCost += verticalCut[idxV] * countH
                countV += 1
                idxV += 1

        return totalCost