class Solution:
    def canReachCorner(self, xCorner, yCorner, circles):
        def is_inside_circle(px, py, cx, cy, radius):
            dx = px - cx
            dy = py - cy
            return dx * dx + dy * dy <= radius * radius

        def touches_left_or_top_edge(cx, cy, r):
            leftEdge = abs(cx) <= r and 0 <= cy <= yCorner
            topEdge = abs(cy - yCorner) <= r and 0 <= cx <= xCorner
            return leftEdge or topEdge

        def touches_right_or_bottom_edge(cx, cy, r):
            rightEdge = abs(cx - xCorner) <= r and 0 <= cy <= yCorner
            bottomEdge = abs(cy) <= r and 0 <= cx <= xCorner
            return rightEdge or bottomEdge

        def explore(i):
            x1, y1, r1 = circles[i]
            if touches_right_or_bottom_edge(x1, y1, r1):
                return True
            vis[i] = True
            for j in range(len(circles)):
                if vis[j]:
                    continue
                x2, y2, r2 = circles[j]
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                rad_sum = r1 + r2
                if dist_sq > rad_sum * rad_sum:
                    continue
                if (x1 * r2 + x2 * r1) < rad_sum * xCorner and (y1 * r2 + y2 * r1) < rad_sum * yCorner and explore(j):
                    return True
            return False

        vis = [False] * len(circles)
        for i in range(len(circles)):
            x, y, r = circles[i]
            if is_inside_circle(0, 0, x, y, r) or is_inside_circle(xCorner, yCorner, x, y, r):
                return False
            if not vis[i] and touches_left_or_top_edge(x, y, r) and explore(i):
                return False
        return True