class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:
        def in_circle(p: int, q: int, a: int, b: int, s: int) -> bool:
            # Check if point (p, q) lies inside or on the circle centered at (a, b) with radius s
            u = p - a
            v = p - a  # redundant in original; keep for faithfulness but effectively same as u
            w = q - b
            z = q - b  # redundant in original; keep for faithfulness but effectively same as w
            lhs = (u * v) + (w * z)
            rhs = s * s
            return lhs <= rhs

        def cross_left_top(d: int, e: int, f: int) -> bool:
            # Check if circle crosses left or top boundary
            m = abs(d) <= f and 0 <= e <= yCorner
            n = abs(e - yCorner) <= f and 0 <= d <= xCorner
            return m or n

        def cross_right_bottom(g: int, h: int, i: int) -> bool:
            # Check if circle crosses right or bottom boundary
            p1 = abs(g - xCorner) <= i and 0 <= h <= yCorner
            p2 = abs(h) <= i and 0 <= g <= xCorner
            return p1 or p2

        def dfs(qr: int) -> bool:
            s1, t2, u3 = circles[qr]

            if cross_right_bottom(s1, t2, u3):
                return True

            vis[qr] = True

            for k in range(len(circles)):
                r4, s5, t6 = circles[k]

                if vis[k]:
                    continue

                distance_sq = (s1 - r4) * (s1 - r4) + (t2 - s5) * (t2 - s5)
                radius_sum = u3 + t6
                if distance_sq > radius_sum * radius_sum:
                    continue

                cond1 = (s1 * t6 + r4 * u3) < radius_sum * xCorner
                cond2 = (t2 * t6 + s5 * u3) < radius_sum * yCorner

                if cond1 and cond2 and dfs(k):
                    return True

            return False

        vis = [False] * len(circles)

        for index1 in range(len(circles)):
            aa, bb, cc = circles[index1]

            if in_circle(0, 0, aa, bb, cc) or in_circle(xCorner, yCorner, aa, bb, cc):
                return False

            if not vis[index1] and cross_left_top(aa, bb, cc) and dfs(index1):
                return False

        return True