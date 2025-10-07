from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        count = 0
        boundary = -1
        index = 0
        points.sort(key=lambda p: p[0])
        while index < len(points):
            coord_x = points[index][0]
            if boundary < coord_x:
                boundary = coord_x + w
                count += 1
            index += 1
        return count