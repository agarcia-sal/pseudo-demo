from typing import List

class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        cnt = 0
        threshold_x = -1
        points.sort(key=lambda p: p[0])

        idx = 0
        while idx < len(points):
            px = points[idx][0]
            py = points[idx][1]

            if not (px <= threshold_x):
                threshold_x = px + w
                cnt += 1
            idx += 1

        return cnt