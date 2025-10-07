class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        # Check if point (x, y) is within or on the circle centered at (cx, cy) with radius r
        def in_circle(x, y, cx, cy, r):
            dx = x - cx
            dy = y - cy
            dist_sq = dx * dx + dy * dy
            r_sq = r * r
            return dist_sq <= r_sq

        # Check if the circle centered at (cx, cy) with radius r crosses the left or top border
        def cross_left_top(cx, cy, r):
            cond1 = abs(cx) <= r and 0 <= cy <= yCorner
            cond2 = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return cond1 or cond2

        # Check if the circle centered at (cx, cy) with radius r crosses the right or bottom border
        def cross_right_bottom(cx, cy, r):
            cond1 = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            cond2 = abs(cy) <= r and 0 <= cx <= xCorner
            return cond1 or cond2

        vis = [False] * len(circles)

        def dfs(current_index):
            cx, cy, cr = circles[current_index]

            if cross_right_bottom(cx, cy, cr):
                return True

            vis[current_index] = True

            for k in range(len(circles)):
                if vis[k]:
                    continue

                nx, ny, nr = circles[k]

                ddx = cx - nx
                ddy = cy - ny
                dist_check = ddx * ddx + ddy * ddy
                rad_sum = cr + nr
                rad_sum_sq = rad_sum * rad_sum

                if dist_check > rad_sum_sq:
                    continue

                left_expr = cx * nr + nx * cr
                right_expr = rad_sum * xCorner
                top_expr = cy * nr + ny * cr
                bottom_expr = rad_sum * yCorner

                if left_expr < right_expr and top_expr < bottom_expr and dfs(k):
                    return True

            return False

        for iter_m in range(len(circles)):
            cur_x, cur_y, cur_r = circles[iter_m]

            if in_circle(0, 0, cur_x, cur_y, cur_r) or in_circle(xCorner, yCorner, cur_x, cur_y, cur_r):
                return False

            if not vis[iter_m]:
                if cross_left_top(cur_x, cur_y, cur_r):
                    if dfs(iter_m):
                        return False

        return True