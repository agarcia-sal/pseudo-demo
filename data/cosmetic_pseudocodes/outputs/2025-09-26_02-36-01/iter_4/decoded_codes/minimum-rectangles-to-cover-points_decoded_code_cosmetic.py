from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        sortedPoints = sorted(points, key=lambda p: p[0])
        countRectangles = 0
        boundaryX = float('-inf')
        index = 0
        while index < len(sortedPoints):
            posX, _ = sortedPoints[index]
            if posX > boundaryX:
                boundaryX = posX + w
                countRectangles += 1
            index += 1
        return countRectangles