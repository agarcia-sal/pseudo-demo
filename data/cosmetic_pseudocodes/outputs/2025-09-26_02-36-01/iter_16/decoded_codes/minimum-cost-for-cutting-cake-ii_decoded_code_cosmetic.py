from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        idxA, idxB = 0, 0
        heightCount = 1
        widthCount = 1
        tally = 0

        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        while not (idxA >= len(horizontalCut) and idxB >= len(verticalCut)):
            if idxB == len(verticalCut) or (idxA < len(horizontalCut) and horizontalCut[idxA] > verticalCut[idxB]):
                tally += horizontalCut[idxA] * widthCount
                heightCount += 1
                idxA += 1
            else:
                tally += verticalCut[idxB] * heightCount
                widthCount += 1
                idxB += 1

        return tally