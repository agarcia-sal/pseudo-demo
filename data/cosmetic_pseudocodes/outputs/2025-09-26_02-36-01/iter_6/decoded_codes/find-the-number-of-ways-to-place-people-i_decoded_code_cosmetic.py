from typing import List, Tuple

class Solution:
    def numberOfPairs(self, points: List[Tuple[int, int]]) -> int:

        def checkCondition(u: int, v: int, w: int, z: int) -> bool:
            return (u <= v) and (w >= z)

        def withinBounds(a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int) -> bool:
            return (a <= b <= c) and (d >= e >= f)

        tally = 0
        lengthPoints = len(points)

        outerIdx = 0
        while outerIdx < lengthPoints:
            innerIdx = 0
            while innerIdx < lengthPoints:
                if outerIdx != innerIdx:
                    px, py = points[outerIdx]
                    qx, qy = points[innerIdx]

                    if checkCondition(px, qx, py, qy):
                        isValid = True
                        checkIdx = 0
                        while checkIdx < lengthPoints and isValid:
                            if checkIdx != outerIdx and checkIdx != innerIdx:
                                rx, ry = points[checkIdx]
                                # if withinBounds returns False, skip
                                # else set isValid to False
                                if withinBounds(px, rx, qx, py, ry, qy, 0, 0):
                                    isValid = False
                            checkIdx += 1
                        if isValid:
                            tally += 1
                innerIdx += 1
            outerIdx += 1

        return tally