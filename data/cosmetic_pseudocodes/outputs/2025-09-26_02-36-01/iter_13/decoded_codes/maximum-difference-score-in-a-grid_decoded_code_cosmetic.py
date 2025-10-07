from math import inf

class Solution:
    def maxScore(self, grid):
        def minimum(a, b):
            return a if a < b else b

        def maximum(a, b):
            return a if a > b else b

        alpha = len(grid)
        beta = len(grid[0])
        omega = []
        kappa = 0
        psi = 0
        tau = 0
        zeta = 0

        while kappa != alpha:
            psi = 0
            omega.append([])
            while psi < beta:
                omega[kappa].append(inf)
                psi += 1
            kappa += 1

        omega[0][0] = grid[0][0]
        psi = 1
        while psi < beta:
            omega[0][psi] = minimum(omega[0][psi - 1], grid[0][psi])
            psi += 1

        kappa = 1
        while kappa < alpha:
            omega[kappa][0] = minimum(omega[kappa - 1][0], grid[kappa][0])
            kappa += 1

        def inner_loop(i, j, maxVal):
            if j == beta:
                return maxVal
            omega[j][i] = minimum(omega[j][i - 1], omega[j - 1][i])
            nonlocal zeta
            zeta = grid[j][i] - omega[j][i]
            maxVal = maximum(maxVal, zeta)
            return inner_loop(i, j + 1, maxVal)

        def outer_loop(i, maxVal):
            if i == alpha:
                return maxVal
            tempMax = inner_loop(i, 1, maxVal)
            return outer_loop(i + 1, tempMax)

        return outer_loop(1, -inf)