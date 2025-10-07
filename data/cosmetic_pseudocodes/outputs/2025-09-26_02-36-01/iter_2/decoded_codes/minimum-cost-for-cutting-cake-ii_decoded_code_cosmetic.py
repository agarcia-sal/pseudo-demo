from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        result = 0
        idxH, idxV = 0, 0
        heightSegments, widthSegments = 1, 1

        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while idxH < len(horizontalCut) or idxV < len(verticalCut):
            if idxV == len(verticalCut) or (idxH < len(horizontalCut) and horizontalCut[idxH] > verticalCut[idxV]):
                tempVal = horizontalCut[idxH]
                result += tempVal * widthSegments
                heightSegments += 1
                idxH += 1
            else:
                tempVal = verticalCut[idxV]
                result += tempVal * heightSegments
                widthSegments += 1
                idxV += 1

        return result