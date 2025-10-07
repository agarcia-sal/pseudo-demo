class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        def in_circle(px: int, py: int, cx: int, cy: int, r: int) -> bool:
            dx = px - cx
            dy = py - cy
            dist_sq = dx * dx + dy * dy
            radius_sq = r * r
            return dist_sq <= radius_sq

        def cross_left_top(cx: int, cy: int, r: int) -> bool:
            cond_1 = (abs(cx) <= r) and (0 <= cy <= yCorner)
            cond_2 = (abs(cy - yCorner) <= r) and (0 <= cx <= xCorner)
            return cond_1 or cond_2

        def cross_right_bottom(cx: int, cy: int, r: int) -> bool:
            cond_1 = (abs(cx - xCorner) <= r) and (0 <= cy <= yCorner)
            cond_2 = (abs(cy) <= r) and (0 <= cx <= xCorner)
            return cond_1 or cond_2

        def dfs(index: int) -> bool:
            cx1, cy1, r1 = circles[index]

            if cross_right_bottom(cx1, cy1, r1):
                return True

            vis[index] = True

            for j, (cx2, cy2, r2) in enumerate(circles):
                if vis[j]:
                    continue

                dx = cx1 - cx2
                dy = cy1 - cy2
                dist_sq = dx * dx + dy * dy
                combined_r = r1 + r2
                combined_r_sq = combined_r * combined_r

                if dist_sq > combined_r_sq:
                    continue

                left_expr_x = cx1 * r2 + cx2 * r1
                right_expr_x = combined_r * xCorner
                left_expr_y = cy1 * r2 + cy2 * r1
                right_expr_y = combined_r * yCorner

                if left_expr_x < right_expr_x and left_expr_y < right_expr_y and dfs(j):
                    return True

            return False

        vis = [False] * len(circles)

        for idx, (cx, cy, r) in enumerate(circles):
            if in_circle(0, 0, cx, cy, r) or in_circle(xCorner, yCorner, cx, cy, r):
                return False

            if not vis[idx] and cross_left_top(cx, cy, r) and dfs(idx):
                return False

        return True