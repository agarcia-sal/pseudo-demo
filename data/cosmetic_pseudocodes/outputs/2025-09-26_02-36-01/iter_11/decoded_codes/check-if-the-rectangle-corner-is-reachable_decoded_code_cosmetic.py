class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        def check_inside_circle(a: int, b: int, c: int, d: int, e: int) -> bool:
            # Check if point (a,b) lies inside or on circle centered at (c,d) with radius e
            return (a - c) ** 2 + (b - d) ** 2 <= e * e

        def touches_left_or_top_edge(p: int, q: int, s: int) -> bool:
            # Check if circle with center (p,q) and radius s touches left edge (x=0) or top edge (y=yCorner)
            cond1 = abs(p) <= s and 0 <= q <= yCorner
            cond2 = abs(q - yCorner) <= s and 0 <= p <= xCorner
            return cond1 or cond2

        def touches_right_or_bottom_edge(p: int, q: int, s: int) -> bool:
            # Check if circle with center (p,q) and radius s touches right edge (x=xCorner) or bottom edge (y=0)
            cond1 = abs(p - xCorner) <= s and 0 <= q <= yCorner
            cond2 = abs(q) <= s and 0 <= p <= xCorner
            return cond1 or cond2

        def traverse_depth(idx: int) -> bool:
            cx, cy, cr = circles[idx]
            if touches_right_or_bottom_edge(cx, cy, cr):
                return True
            vis[idx] = True

            for iter_idx, (nx, ny, nr) in enumerate(circles):
                if vis[iter_idx]:
                    continue
                dist_sq = (cx - nx) ** 2 + (cy - ny) ** 2
                if dist_sq > (cr + nr) ** 2:
                    continue

                condX = cx * nr + nx * cr < (cr + nr) * xCorner
                condY = cy * nr + ny * cr < (cr + nr) * yCorner

                if condX and condY and traverse_depth(iter_idx):
                    return True

            return False

        vis = [False] * len(circles)

        for idx2, (cx2, cy2, cr2) in enumerate(circles):
            if check_inside_circle(0, 0, cx2, cy2, cr2) or check_inside_circle(xCorner, yCorner, cx2, cy2, cr2):
                return False
            if (not vis[idx2]) and touches_left_or_top_edge(cx2, cy2, cr2) and traverse_depth(idx2):
                return False

        return True