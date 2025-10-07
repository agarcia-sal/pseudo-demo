class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: list[list[int]]) -> bool:

        def inside_circle(a: int, b: int, c: int, d: int, e: int) -> bool:
            return (a - c) ** 2 + (b - d) ** 2 <= e * e

        def touches_left_or_top(s: int, t: int, u: int) -> bool:
            cond1 = abs(s) <= u and 0 <= t <= yCorner
            cond2 = abs(t - yCorner) <= u and 0 <= s <= xCorner
            return cond1 or cond2

        def touches_right_or_bottom(p: int, q: int, r: int) -> bool:
            condA = abs(p - xCorner) <= r and 0 <= q <= yCorner
            condB = abs(q) <= r and 0 <= p <= xCorner
            return condA or condB

        vis = [False] * len(circles)

        def explore(w: int) -> bool:
            cx, cy, rad = circles[w]
            if touches_right_or_bottom(cx, cy, rad):
                return True
            vis[w] = True

            def recur_loop(idx: int, lst: list[list[int]]) -> bool:
                if idx >= len(lst):
                    return False
                nx, ny, nr = lst[idx]
                if vis[idx]:
                    return recur_loop(idx + 1, lst)
                dist_sq = (cx - nx) ** 2 + (cy - ny) ** 2
                rad_sum = rad + nr
                if dist_sq > rad_sum * rad_sum:
                    return recur_loop(idx + 1, lst)
                cond_x = (cx * nr + nx * rad) < (rad_sum * xCorner)
                cond_y = (cy * nr + ny * rad) < (rad_sum * yCorner)
                if cond_x and cond_y and explore(idx):
                    return True
                return recur_loop(idx + 1, lst)

            return recur_loop(0, circles)

        def main_loop(sz: int) -> bool:
            if sz >= len(circles):
                return True
            x, y, r = circles[sz]
            if inside_circle(0, 0, x, y, r) or inside_circle(xCorner, yCorner, x, y, r):
                return False
            if not vis[sz] and touches_left_or_top(x, y, r) and explore(sz):
                return False
            return main_loop(sz + 1)

        return main_loop(0)