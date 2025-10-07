from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def compareBounds(a: int, b: int, c: int, d: int) -> bool:
            return a <= c and b >= d

        accumulator = 0
        total = len(points)

        for outerIndex in range(total):
            for innerIndex in range(total):
                if outerIndex != innerIndex:
                    px, py = points[outerIndex]
                    qx, qy = points[innerIndex]
                    if compareBounds(px, py, qx, qy):
                        isValid = True
                        for checkIndex in range(total):
                            if checkIndex != outerIndex and checkIndex != innerIndex:
                                rx, ry = points[checkIndex]
                                if px <= rx <= qx and py >= ry >= qy:
                                    isValid = False
                                    break
                        if isValid:
                            accumulator += 1
        return accumulator