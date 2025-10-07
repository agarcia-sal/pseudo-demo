from math import fabs

class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):

        def circle_contains_point(a, b, c, d, e):
            # Check if point (a,b) is inside circle centered at (c,d) with radius e
            temp1 = a - c
            temp2 = temp1 * temp1
            temp3 = b - d
            temp4 = temp3 * temp3
            lhs = temp2 + temp4
            rhs = e * e
            return lhs <= rhs

        def check_left_top_wall(c, d, e):
            cond1_part1 = (fabs(c) <= e)
            cond1_part2 = (0 <= d)
            cond1_part3 = (d <= yCorner)
            cond1 = cond1_part1 and cond1_part2 and cond1_part3

            cond2_part1 = (fabs(d - yCorner) <= e)
            cond2_part2 = (0 <= c)
            cond2_part3 = (c <= xCorner)
            cond2 = cond2_part1 and cond2_part2 and cond2_part3

            return cond1 or cond2

        def check_right_bottom_wall(c, d, e):
            cond1_part1 = (fabs(c - xCorner) <= e)
            cond1_part2 = (0 <= d)
            cond1_part3 = (d <= yCorner)
            cond1 = cond1_part1 and cond1_part2 and cond1_part3

            cond2_part1 = (fabs(d) <= e)
            cond2_part2 = (0 <= c)
            cond2_part3 = (c <= xCorner)
            cond2 = cond2_part1 and cond2_part2 and cond2_part3

            return cond1 or cond2

        vis = [False] * len(circles)

        def explore(index):
            x_val, y_val, radius_val = circles[index]

            if check_right_bottom_wall(x_val, y_val, radius_val):
                return True

            vis[index] = True

            for k in range(len(circles)):
                x2_val, y2_val, radius2_val = circles[k]

                if vis[k]:
                    skip_flag = True
                else:
                    dx = x_val - x2_val
                    dy = y_val - y2_val
                    dist_sq = dx * dx + dy * dy
                    rad_sum = radius_val + radius2_val
                    rad_sum_sq = rad_sum * rad_sum
                    if dist_sq > rad_sum_sq:
                        skip_flag = True
                    else:
                        skip_flag = False

                if skip_flag:
                    continue

                cond_x = (x_val * radius2_val + x2_val * radius_val) < (rad_sum * xCorner)
                cond_y = (y_val * radius2_val + y2_val * radius_val) < (rad_sum * yCorner)
                if cond_x and cond_y and explore(k):
                    return True

            return False

        for idx in range(len(circles)):
            cx, cy, cr = circles[idx]

            if circle_contains_point(0, 0, cx, cy, cr) or circle_contains_point(xCorner, yCorner, cx, cy, cr):
                return False
            if not vis[idx]:
                if check_left_top_wall(cx, cy, cr):
                    if explore(idx):
                        return False

        return True