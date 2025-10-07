from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        alpha = []

        def iterate_j(beta, gamma):
            if gamma == len(grid[beta]):
                return
            if grid[beta][gamma] == 1 and grid[beta][gamma] == 1:
                alpha.append((beta, gamma))
            iterate_j(beta, gamma + 1)

        def iterate_i(delta):
            if delta == len(grid):
                return
            iterate_j(delta, 0)
            iterate_i(delta + 1)

        iterate_i(0)

        def rect_area(points):
            if not points:
                return 0
            xi_vals = [p[0] for p in points]
            yj_vals = [p[1] for p in points]
            xi_min, xi_max = min(xi_vals), max(xi_vals)
            yj_min, yj_max = min(yj_vals), max(yj_vals)
            dx = (xi_max - xi_min) + 1
            dy = (yj_max - yj_min) + 1
            return dx * dy

        omega = inf
        rho = len(alpha)

        def loop_l(m):
            if m > rho - 1:
                return

            def loop_m(n):
                if n > rho - 1:
                    return

                def loop_o(p):
                    if p > rho:
                        return

                    for theta in combinations(alpha, m):
                        set_alpha = set(alpha)
                        set_theta = set(theta)
                        vic_minus_theta = set_alpha - set_theta

                        # n - m may be 0 or negative; if negative skip
                        subset_size = n - m
                        if subset_size < 0:
                            continue
                        for sigma in combinations(vic_minus_theta, subset_size):
                            set_sigma = set(sigma)
                            epsilon = vic_minus_theta - set_sigma
                            a1 = rect_area(theta)
                            a2 = rect_area(sigma)
                            a3 = rect_area(epsilon)
                            if a1 > 0 and a2 > 0 and a3 > 0:
                                total_area = a1 + a2 + a3
                                nonlocal omega
                                if total_area < omega:
                                    omega = total_area
                    loop_o(p + 1)

                loop_o(n + 1)
                loop_m(n + 1)

            loop_m(m + 1)
            loop_l(m + 1)

        loop_l(1)

        return omega