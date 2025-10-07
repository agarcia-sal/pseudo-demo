class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        vis = [False] * len(circles)

        def in_circle(x, y, cx, cy, r):
            dx = x - cx
            dy = y - cy
            dist_sq = dx * dx + dy * dy
            r_sq = r * r
            return dist_sq <= r_sq

        def cross_left_top(cx, cy, r):
            abs_cx = cx if cx >= 0 else -cx
            condA = (abs_cx <= r) and (0 <= cy <= yCorner)
            abs_diff_cy = cy - yCorner
            abs_diff_cy = abs_diff_cy if abs_diff_cy >= 0 else -abs_diff_cy
            condB = (abs_diff_cy <= r) and (0 <= cx <= xCorner)
            return condA or condB

        def cross_right_bottom(cx, cy, r):
            diff_cx = cx - xCorner
            diff_cx = diff_cx if diff_cx >= 0 else -diff_cx
            condA = (diff_cx <= r) and (0 <= cy <= yCorner)
            abs_cy = cy if cy >= 0 else -cy
            condB = (abs_cy <= r) and (0 <= cx <= xCorner)
            return condA or condB

        def dfs(index):
            cx1, cy1, rad1 = circles[index]
            if cross_right_bottom(cx1, cy1, rad1):
                return True
            vis[index] = True

            def iterate_j(j_val):
                if j_val >= len(circles):
                    return False
                if vis[j_val]:
                    return iterate_j(j_val + 1)
                cx2, cy2, rad2 = circles[j_val]
                delta_x = cx1 - cx2
                delta_y = cy1 - cy2
                dist_sq = delta_x * delta_x + delta_y * delta_y
                sum_rad = rad1 + rad2
                sum_rad_sq = sum_rad * sum_rad
                if dist_sq > sum_rad_sq:
                    return iterate_j(j_val + 1)
                lhs_x = (cx1 * rad2) + (cx2 * rad1)
                rhs_x = (rad1 + rad2) * xCorner
                lhs_y = (cy1 * rad2) + (cy2 * rad1)
                rhs_y = (rad1 + rad2) * yCorner
                if (lhs_x < rhs_x) and (lhs_y < rhs_y):
                    if dfs(j_val):
                        return True
                return iterate_j(j_val + 1)

            return iterate_j(0)

        def loop_i(i_val):
            if i_val >= len(circles):
                return True
            cx, cy, rad = circles[i_val]
            if in_circle(0, 0, cx, cy, rad) or in_circle(xCorner, yCorner, cx, cy, rad):
                return False
            if not vis[i_val] and cross_left_top(cx, cy, rad) and dfs(i_val):
                return False
            return loop_i(i_val + 1)

        return loop_i(0)