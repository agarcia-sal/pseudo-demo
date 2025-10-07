from typing import List, Tuple


class Solution:
    def canReachCorner(self, xCorner: int, yCorner: int, circles: List[Tuple[int, int, int]]) -> bool:
        def in_circle(alpha: int, beta: int, gamma: int, delta: int, epsilon: int) -> bool:
            part1 = (alpha - gamma) ** 2
            part2 = (beta - delta) ** 2
            limit = epsilon ** 2
            return (part1 + part2) <= limit

        def cross_left_top(chi: int, psi: int, rho: int) -> bool:
            cond1 = abs(chi) <= rho and 0 <= psi <= yCorner
            cond2 = abs(psi - yCorner) <= rho and 0 <= chi <= xCorner
            return cond1 or cond2

        def cross_right_bottom(zeta: int, eta: int, theta: int) -> bool:
            cond3 = abs(zeta - xCorner) <= theta and 0 <= eta <= yCorner
            cond4 = abs(eta) <= theta and 0 <= zeta <= xCorner
            return cond3 or cond4

        def dfs(m: int) -> bool:
            A, B, C = circles[m]
            if cross_right_bottom(A, B, C):
                return True
            vis[m] = True

            for n in range(len(circles)):
                if vis[n]:
                    continue
                D, E, F = circles[n]

                dist_sq = (A - D) ** 2 + (B - E) ** 2
                rad_sum = C + F
                if dist_sq > rad_sum ** 2:
                    continue

                condX = (A * F + D * C) < rad_sum * xCorner
                condY = (B * F + E * C) < rad_sum * yCorner

                if condX and condY and dfs(n):
                    return True
            return False

        vis = [False] * len(circles)
        for idx, (p, q, r) in enumerate(circles):
            if in_circle(0, 0, p, q, r) or in_circle(xCorner, yCorner, p, q, r):
                return False
            if not vis[idx] and cross_left_top(p, q, r) and dfs(idx):
                return False
        return True