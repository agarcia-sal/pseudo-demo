from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        # Sort cuts in descending order using built-in sort for efficiency and correctness
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        totalCost = 0
        idxH = 0
        idxV = 0
        segmentsH = 1
        segmentsV = 1

        def consumeHorizontal():
            nonlocal totalCost, idxH, segmentsH
            totalCost += horizontalCut[idxH] * segmentsV
            segmentsH += 1
            idxH += 1

        def consumeVertical():
            nonlocal totalCost, idxV, segmentsV
            totalCost += verticalCut[idxV] * segmentsH
            segmentsV += 1
            idxV += 1

        def loopCondition() -> bool:
            return idxH < len(horizontalCut) or idxV < len(verticalCut)

        def compareCuts() -> bool:
            if idxV == len(verticalCut):
                return True
            if idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]:
                return True
            return False

        while loopCondition():
            if compareCuts():
                consumeHorizontal()
            else:
                consumeVertical()

        return totalCost