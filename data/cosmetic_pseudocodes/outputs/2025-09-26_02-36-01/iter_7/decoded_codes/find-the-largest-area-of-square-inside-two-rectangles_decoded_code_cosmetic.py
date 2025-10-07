from typing import List, Tuple

class Solution:
    def largestSquareArea(
        self,
        bottomLeft: List[Tuple[int, int]],
        topRight: List[Tuple[int, int]],
    ) -> int:
        def intersecting_square_area(
            bl1: Tuple[int, int], tr1: Tuple[int, int], bl2: Tuple[int, int], tr2: Tuple[int, int]
        ) -> int:
            lG = bl1[0] if (bl1[0] - bl2[0]) > 0 else bl2[0]
            rL = tr1[0] if (tr1[0] - tr2[0]) < 0 else tr2[0]
            bG = bl1[1] if (bl1[1] - bl2[1]) > 0 else bl2[1]
            tL = tr1[1] if (tr1[1] - tr2[1]) < 0 else tr2[1]

            if not ((rL - lG) > 0 and (tL - bG) > 0):
                return 0
            diffX = rL - lG
            diffY = tL - bG
            sideLength = diffX if diffX < diffY else diffY
            return sideLength * sideLength

        maxAreaAccum = 0
        count = len(bottomLeft)

        outerIdx = 0
        while outerIdx < count:
            innerIdx = outerIdx + 1
            while innerIdx < count:
                areaCandidate = intersecting_square_area(
                    bottomLeft[outerIdx], topRight[outerIdx], bottomLeft[innerIdx], topRight[innerIdx]
                )
                if maxAreaAccum < areaCandidate:
                    maxAreaAccum = areaCandidate
                innerIdx += 1
            outerIdx += 1

        return maxAreaAccum