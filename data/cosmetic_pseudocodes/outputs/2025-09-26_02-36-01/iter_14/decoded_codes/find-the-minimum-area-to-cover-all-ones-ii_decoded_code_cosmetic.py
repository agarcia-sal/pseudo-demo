from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        alpha = []
        z = 0
        while z < len(grid):
            omega = 0
            while omega < len(grid[z]):
                if grid[z][omega] == 1:
                    alpha.append((z, omega))
                omega += 1
            z += 1

        def rect_area(points):
            if len(points) == 0:
                return 0
            sigma = [point[0] for point in points]
            mu = [point[1] for point in points]
            xi = max(sigma) - min(sigma) + 1
            psi = max(mu) - min(mu) + 1
            return xi * psi

        beta = inf
        gamma = len(alpha)

        i = 1
        while i < gamma:
            j = i + 1
            while j < gamma:
                k = j + 1
                while True:
                    def internal_loop():
                        set_alpha = set(alpha)
                        for comb1 in combinations(alpha, i):
                            set_comb1 = set(comb1)
                            rem1 = set_alpha - set_comb1
                            if len(rem1) < (j - i):
                                continue
                            for comb2 in combinations(rem1, j - i):
                                set_comb2 = set(comb2)
                                comb3 = rem1 - set_comb2
                                a1 = rect_area(comb1)
                                a2 = rect_area(comb2)
                                a3 = rect_area(comb3)
                                if a1 > 0 and a2 > 0 and a3 > 0:
                                    curr_sum = a1 + a2 + a3
                                    nonlocal beta
                                    if curr_sum < beta:
                                        beta = curr_sum
                    internal_loop()
                    k += 1
                    if k > gamma:
                        break
                j += 1
            i += 1

        return beta