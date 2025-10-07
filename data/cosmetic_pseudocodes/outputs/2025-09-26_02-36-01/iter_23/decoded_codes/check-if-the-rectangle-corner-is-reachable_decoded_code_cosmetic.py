class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        vis = [False] * len(circles)

        def check_inside_circle(a, b, c, d, e):
            dx = a - c
            dy = b - d
            return dx * dx + dy * dy <= e * e

        def touches_left_or_top_edge(cx, cy, r):
            cond1 = abs(cx) <= r and 0 <= cy <= yCorner
            cond2 = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return cond1 or cond2

        def touches_right_or_bottom_edge(cx, cy, r):
            cond3 = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            cond4 = abs(cy) <= r and 0 <= cx <= xCorner
            return cond3 or cond4

        def recursive_search(k):
            posX, posY, radius = circles[k]

            if touches_right_or_bottom_edge(posX, posY, radius):
                return True

            vis[k] = True

            def iterate_over_circles(m):
                if m >= len(circles):
                    return False

                if vis[m]:
                    return iterate_over_circles(m + 1)

                curX, curY, curR = circles[m]

                dx = posX - curX
                dy = posY - curY
                dist_sq = dx * dx + dy * dy
                rad_sum = radius + curR
                rad_sum_sq = rad_sum * rad_sum

                if dist_sq > rad_sum_sq:
                    return iterate_over_circles(m + 1)

                weighted_x_sum = (posX * curR) + (curX * radius)
                weighted_x_limit = rad_sum * xCorner

                weighted_y_sum = (posY * curR) + (curY * radius)
                weighted_y_limit = rad_sum * yCorner

                if weighted_x_sum < weighted_x_limit and weighted_y_sum < weighted_y_limit:
                    if recursive_search(m):
                        return True

                return iterate_over_circles(m + 1)

            return iterate_over_circles(0)

        def check_circles(index):
            if index >= len(circles):
                return True

            cx, cy, cr = circles[index]

            if check_inside_circle(0, 0, cx, cy, cr) or check_inside_circle(xCorner, yCorner, cx, cy, cr):
                return False

            if not vis[index] and touches_left_or_top_edge(cx, cy, cr):
                if recursive_search(index):
                    return False

            return check_circles(index + 1)

        return check_circles(0)