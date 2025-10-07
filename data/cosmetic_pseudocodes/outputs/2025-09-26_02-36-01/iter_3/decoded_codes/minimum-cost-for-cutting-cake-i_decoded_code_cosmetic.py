class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: list[int], verticalCut: list[int]) -> int:
        totalCost = 0
        idxH = 0
        idxV = 0
        countH = 1
        countV = 1

        reversedHC = horizontalCut[::-1]
        reversedVC = verticalCut[::-1]

        while idxH < m - 1 or idxV < n - 1:
            if idxV == n - 1 or (idxH < m - 1 and reversedHC[idxH] > reversedVC[idxV]):
                val = reversedHC[idxH]
                addVal = val * countV  # sum val countV times
                totalCost += addVal
                countH += 1
                idxH += 1
            else:
                val = reversedVC[idxV]
                addVal = val * countH  # sum val countH times
                totalCost += addVal
                countV += 1
                idxV += 1
        return totalCost