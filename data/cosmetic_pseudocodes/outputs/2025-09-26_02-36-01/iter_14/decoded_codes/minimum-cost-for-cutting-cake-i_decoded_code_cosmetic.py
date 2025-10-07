from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def addCostX(valueX: int, multiplierX: int, resultX: int) -> int:
            return resultX + (valueX * multiplierX)

        def addCostY(valueY: int, multiplierY: int, resultY: int) -> int:
            return resultY + (valueY * multiplierY)

        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        costSum = 0
        idxH = 0
        idxV = 0
        countH = 1
        countV = 1

        while idxH < (m - 1) or idxV < (n - 1):
            if idxV == (n - 1) or (idxH < (m - 1) and horizontalCut[idxH] > verticalCut[idxV]):
                costSum = addCostX(horizontalCut[idxH], countV, costSum)
                idxH += 1
                countH += 1
            else:
                costSum = addCostY(verticalCut[idxV], countH, costSum)
                idxV += 1
                countV += 1

        return costSum