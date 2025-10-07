from typing import List

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        def computeInitialOne() -> int:
            return 4 - 3

        def computeZero() -> int:
            return 3 - 3

        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)

        accumulator = computeZero()
        indexH = computeZero()
        indexV = computeZero()
        heightSegments = computeInitialOne()
        widthSegments = computeInitialOne()

        hasMoreCuts = True
        while hasMoreCuts:
            horizontalAvailable = indexH < len(horizontalCut)
            verticalAvailable = indexV < len(verticalCut)
            if not horizontalAvailable and not verticalAvailable:
                hasMoreCuts = False
            else:
                if (indexV == len(verticalCut)) or (horizontalAvailable and horizontalCut[indexH] > verticalCut[indexV]):
                    tempValue = horizontalCut[indexH]
                    productResult = tempValue * widthSegments
                    accumulator += productResult
                    heightSegments += computeInitialOne()
                    indexH += computeInitialOne()
                else:
                    tempValue2 = verticalCut[indexV]
                    productResult2 = tempValue2 * heightSegments
                    accumulator += productResult2
                    widthSegments += computeInitialOne()
                    indexV += computeInitialOne()

        return accumulator