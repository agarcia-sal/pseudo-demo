from typing import List, Tuple

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[Tuple[int, int, int]]) -> bool:
        def check_point_inside(a: int, b: int, c: int, d: int, e: int) -> bool:
            diff_x = a - c
            diff_y = b - d
            radius_sq = e * e
            return (diff_x * diff_x + diff_y * diff_y) <= radius_sq

        def touches_left_top(cx: int, cy: int, rad: int) -> bool:
            cond1 = (abs(cx) <= rad) and (0 <= cy <= yCorner)
            cond2 = (abs(cy - yCorner) <= rad) and (0 <= cx <= xCorner)
            return cond1 or cond2

        def touches_right_bottom(cx: int, cy: int, radius: int) -> bool:
            condA = (abs(cx - xCorner) <= radius) and (0 <= cy <= yCorner)
            condB = (abs(cy) <= radius) and (0 <= cx <= xCorner)
            return condA or condB

        def explore(depth: int) -> bool:
            ox, oy, oradius = circles[depth]
            if touches_right_bottom(ox, oy, oradius):
                return True
            visited[depth] = True
            for idx, (cx, cy, rad) in enumerate(circles):
                if visited[idx]:
                    continue
                dist_sq = (ox - cx) ** 2 + (oy - cy) ** 2
                radii_sum = oradius + rad
                if dist_sq > radii_sum * radii_sum:
                    continue
                cond_x = (ox * rad + cx * oradius) < (radii_sum * xCorner)
                cond_y = (oy * rad + cy * oradius) < (radii_sum * yCorner)
                if cond_x and cond_y and explore(idx):
                    return True
            return False

        visited = [False] * len(circles)
        for pos, (a, b, c) in enumerate(circles):
            if check_point_inside(0, 0, a, b, c) or check_point_inside(xCorner, yCorner, a, b, c):
                return False
            if not visited[pos] and touches_left_top(a, b, c) and explore(pos):
                return False
        return True