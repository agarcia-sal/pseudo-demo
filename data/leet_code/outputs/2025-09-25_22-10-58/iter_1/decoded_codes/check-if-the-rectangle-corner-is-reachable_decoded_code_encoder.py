class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def in_circle(x, y, cx, cy, r):
            return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

        def cross_left_top(cx, cy, r):
            condition_a = abs(cx) <= r and 0 <= cy <= yCorner
            condition_b = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return condition_a or condition_b

        def cross_right_bottom(cx, cy, r):
            condition_a = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            condition_b = abs(cy) <= r and 0 <= cx <= xCorner
            return condition_a or condition_b

        def dfs(i):
            x1, y1, r1 = circles[i]
            if cross_right_bottom(x1, y1, r1):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                if vis[j]:
                    continue
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if dist_sq > (r1 + r2) ** 2:
                    continue
                # Check if circles intersect within grid bounds before DFS to avoid invalid moves
                if (x1 * r2 + x2 * r1 < (r1 + r2) * xCorner and
                        y1 * r2 + y2 * r1 < (r1 + r2) * yCorner and
                        dfs(j)):
                    return True
            return False

        vis = [False] * len(circles)
        for i, (x, y, r) in enumerate(circles):
            if in_circle(0, 0, x, y, r) or in_circle(xCorner, yCorner, x, y, r):
                return False
        for i, (x, y, r) in enumerate(circles):
            if not vis[i] and cross_left_top(x, y, r) and dfs(i):
                return False
        return True