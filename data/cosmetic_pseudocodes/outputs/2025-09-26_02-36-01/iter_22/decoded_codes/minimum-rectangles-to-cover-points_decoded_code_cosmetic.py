from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        count_rectangles = 0
        index_cursor = 0
        points.sort(key=lambda p: p[0])
        n = len(points)
        while index_cursor < n:
            base_position = points[index_cursor][0]
            extended_limit = base_position + w
            count_rectangles += 1
            while index_cursor < n and points[index_cursor][0] < extended_limit:
                index_cursor += 1
        return count_rectangles