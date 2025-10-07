from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        rectangles_count = 0
        latest_covered_x = -1
        points.sort(key=lambda p: p[0])
        for x, _ in points:
            if x > latest_covered_x:
                latest_covered_x = x + w
                rectangles_count += 1
        return rectangles_count