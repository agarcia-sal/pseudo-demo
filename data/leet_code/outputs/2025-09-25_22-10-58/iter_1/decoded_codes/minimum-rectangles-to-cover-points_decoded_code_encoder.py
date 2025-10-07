from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        points.sort(key=lambda p: p[0])
        rectangles = 0
        current_x = -1
        for x, y in points:
            if x > current_x:
                current_x = x + w
                rectangles += 1
        return rectangles