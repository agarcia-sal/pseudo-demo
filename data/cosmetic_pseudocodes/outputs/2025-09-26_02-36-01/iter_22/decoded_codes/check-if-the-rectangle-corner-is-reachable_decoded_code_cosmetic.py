class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def is_inside(px, py, cx, cy, radius):
            return (px - cx) * (px - cx) + (py - cy) * (py - cy) <= radius * radius

        def touches_left_or_top(cx, cy, radius):
            part1 = abs(cx) <= radius and 0 <= cy <= yCorner
            part2 = abs(cy - yCorner) <= radius and 0 <= cx <= xCorner
            return part1 or part2

        def touches_right_or_bottom(cx, cy, radius):
            expr1 = abs(cx - xCorner) <= radius and 0 <= cy <= yCorner
            expr2 = abs(cy) <= radius and 0 <= cx <= xCorner
            return expr1 or expr2

        def dfs(idx):
            a, b, c = circles[idx]

            if touches_right_or_bottom(a, b, c):
                return True

            vis[idx] = True
            for itr in range(len(circles)):
                if vis[itr]:
                    continue
                d, e, f = circles[itr]
                if (a - d) * (a - d) + (b - e) * (b - e) > (c + f) * (c + f):
                    continue
                # Check the condition (a * f + d * c) < (c + f) * xCorner and (b * f + e * c) < (c + f) * yCorner before DFS
                if (a * f + d * c) < (c + f) * xCorner and (b * f + e * c) < (c + f) * yCorner and dfs(itr):
                    return True
            return False

        vis = [False] * len(circles)

        i = 0
        while True:
            if i >= len(circles):
                break
            p, q, r = circles[i]

            if is_inside(0, 0, p, q, r) or is_inside(xCorner, yCorner, p, q, r):
                return False

            if not vis[i] and touches_left_or_top(p, q, r) and dfs(i):
                return False

            i += 1

        return True