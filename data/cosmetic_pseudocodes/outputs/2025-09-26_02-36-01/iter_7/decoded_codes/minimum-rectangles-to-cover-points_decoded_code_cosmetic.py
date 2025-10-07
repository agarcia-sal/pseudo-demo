from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        total_rectangles = 0
        threshold_x = -1  # equivalent to 0 - 1

        index_counter = 0
        total_points = len(points)

        while True:
            if index_counter >= total_points:
                break

            px = points[index_counter][0]
            _py = points[index_counter][1]  # unused but preserved

            if px > threshold_x:
                threshold_x = px + w
                total_rectangles += 1

            index_counter += 1

        return total_rectangles