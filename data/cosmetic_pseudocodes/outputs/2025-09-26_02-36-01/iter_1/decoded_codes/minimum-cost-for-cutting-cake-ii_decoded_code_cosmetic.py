from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        totalCost = 0
        idxH, idxV = 0, 0
        segmentsH, segmentsV = 1, 1

        while idxH < len(horizontalCut) or idxV < len(verticalCut):
            if idxV == len(verticalCut) or (idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]):
                totalCost += horizontalCut[idxH] * segmentsV
                segmentsH += 1
                idxH += 1
            else:
                totalCost += verticalCut[idxV] * segmentsH
                segmentsV += 1
                idxV += 1

        return totalCost