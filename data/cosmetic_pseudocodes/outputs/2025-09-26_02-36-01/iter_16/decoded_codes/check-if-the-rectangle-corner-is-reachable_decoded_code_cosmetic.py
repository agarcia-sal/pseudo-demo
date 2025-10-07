from typing import List, Tuple

class Solution:

    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[Tuple[int, int, int]]) -> bool:

        def circle_includes(px: int, py: int, cx: int, cy: int, radius: int) -> bool:
            dx = px - cx
            dy = py - cy
            dist_squared = dx * dx + dy * dy
            radius_squared = radius * radius
            return dist_squared <= radius_squared

        def touches_left_top(cx: int, cy: int, radius: int) -> bool:
            cond_left_edge = (abs(cx) <= radius) and (0 <= cy <= yCorner)
            cond_top_edge = (abs(cy - yCorner) <= radius) and (0 <= cx <= xCorner)
            return cond_left_edge or cond_top_edge

        def touches_right_bottom(cx: int, cy: int, radius: int) -> bool:
            cond_right_edge = (abs(cx - xCorner) <= radius) and (0 <= cy <= yCorner)
            cond_bottom_edge = (abs(cy) <= radius) and (0 <= cx <= xCorner)
            return cond_right_edge or cond_bottom_edge

        def depth_first_search(index: int) -> bool:
            cx_curr, cy_curr, r_curr = circles[index]
            if touches_right_bottom(cx_curr, cy_curr, r_curr):
                return True
            vis[index] = True
            for j in range(len(circles)):
                if vis[j]:
                    continue
                cx_next, cy_next, r_next = circles[j]
                dx = cx_curr - cx_next
                dy = cy_curr - cy_next
                if dx * dx + dy * dy > (r_curr + r_next) * (r_curr + r_next):
                    continue

                lhs_x = cx_curr * r_next + cx_next * r_curr
                rhs_x = (r_curr + r_next) * xCorner
                lhs_y = cy_curr * r_next + cy_next * r_curr
                rhs_y = (r_curr + r_next) * yCorner

                if lhs_x < rhs_x and lhs_y < rhs_y and depth_first_search(j):
                    return True
            return False

        vis = [False] * len(circles)
        for i in range(len(circles)):
            cx, cy, r = circles[i]
            if circle_includes(0, 0, cx, cy, r) or circle_includes(xCorner, yCorner, cx, cy, r):
                return False
            if not vis[i] and touches_left_top(cx, cy, r) and depth_first_search(i):
                return False
        return True