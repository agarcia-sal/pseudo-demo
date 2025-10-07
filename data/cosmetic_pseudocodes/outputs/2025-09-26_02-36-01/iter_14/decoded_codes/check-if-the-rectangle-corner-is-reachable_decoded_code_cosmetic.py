from typing import List, Tuple

class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[Tuple[int, int, int]]) -> bool:
        # Helper function to check if point (px, py) is inside or on the circle centered at (cx, cy) with radius
        def check_inside(px: int, py: int, cx: int, cy: int, radius: int) -> bool:
            dx = cx - px
            dy = cy - py
            dist_sq = dx * dx + dy * dy
            return dist_sq <= radius * radius

        # Check if circle intersects either coordinate axis segments from (0,0) to (xCorner, yCorner)
        def intersects_left_top(cx: int, cy: int, radius: int) -> bool:
            cond1 = (0 <= cy <= yCorner) and (abs(cx) <= radius)
            dcy = cy - yCorner
            cond2 = (0 <= cx <= xCorner) and (abs(dcy) <= radius)
            return cond1 or cond2

        def intersects_right_bottom(cx: int, cy: int, radius: int) -> bool:
            dct = cx - xCorner
            cond1 = (0 <= cy <= yCorner) and (abs(dct) <= radius)
            cond2 = (0 <= cx <= xCorner) and (abs(cy) <= radius)
            return cond1 or cond2

        visited = [False] * len(circles)

        def depth_search(index: int) -> bool:
            c_x, c_y, c_r = circles[index]
            if intersects_right_bottom(c_x, c_y, c_r):
                return True

            visited[index] = True

            for idx, (p_x, p_y, p_r) in enumerate(circles):
                if visited[idx]:
                    continue
                delta_x = c_x - p_x
                delta_y = c_y - p_y
                sq_dist = delta_x * delta_x + delta_y * delta_y
                radius_sum = c_r + p_r
                if sq_dist > radius_sum * radius_sum:
                    continue

                left_expr = (c_x * p_r) + (p_x * c_r)
                right_bound_x = radius_sum * xCorner
                left_expr_y = (c_y * p_r) + (p_y * c_r)
                right_bound_y = radius_sum * yCorner

                if (left_expr < right_bound_x) and (left_expr_y < right_bound_y) and depth_search(idx):
                    return True
            return False

        for pos, (cir_x, cir_y, cir_r) in enumerate(circles):
            if check_inside(0, 0, cir_x, cir_y, cir_r) or check_inside(xCorner, yCorner, cir_x, cir_y, cir_r):
                return False

            if (not visited[pos]) and intersects_left_top(cir_x, cir_y, cir_r) and depth_search(pos):
                return False

        return True