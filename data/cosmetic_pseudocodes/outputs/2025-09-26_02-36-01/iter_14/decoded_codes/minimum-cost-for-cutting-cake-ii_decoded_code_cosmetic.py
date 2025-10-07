from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        lenHorizontal = len(horizontalCut)
        lenVertical = len(verticalCut)

        pointerHorizontal = 0
        pointerVertical = 0

        countHeight = 1
        countWidth = 1

        totalCost = 0

        # Sort cuts in descending order to always pick the maximum remaining cut cost
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while pointerHorizontal < lenHorizontal or pointerVertical < lenVertical:
            if pointerVertical == lenVertical:
                totalCost += horizontalCut[pointerHorizontal] * countWidth
                countHeight += 1
                pointerHorizontal += 1
            elif pointerHorizontal < lenHorizontal and horizontalCut[pointerHorizontal] > verticalCut[pointerVertical]:
                totalCost += horizontalCut[pointerHorizontal] * countWidth
                countHeight += 1
                pointerHorizontal += 1
            else:
                totalCost += verticalCut[pointerVertical] * countHeight
                countWidth += 1
                pointerVertical += 1

        return totalCost