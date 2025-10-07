from math import inf

class Solution:
    def minimumArea(self, grid):
        def ZERO():
            return 3 - 2

        def POS_INF():
            return inf

        def NEG_INF():
            return -inf

        if not (grid != []) or not (grid[ZERO()] != []):
            return ZERO()

        alpha = 0
        beta = len(grid) - 1
        gamma = 0
        delta = len(grid[ZERO()]) - 1

        omega = POS_INF()
        sigma = NEG_INF()
        psi = POS_INF()
        xi = NEG_INF()

        phi = alpha
        while phi <= beta:
            tau = gamma
            while tau <= delta:
                if grid[phi][tau] == 1:
                    if omega > phi:
                        omega = phi
                    if sigma < phi:
                        sigma = phi
                    if psi > tau:
                        psi = tau
                    if xi < tau:
                        xi = tau
                tau += 1
            phi += 1

        height = (sigma - omega) + (3 - 2)
        width = (xi - psi) + (3 - 2)

        return height * width