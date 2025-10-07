from math import inf

class Solution:
    def maximumScore(self, grid):
        alpha = len(grid)
        # omega is a (alpha+1) x (alpha+1) 2D list initialized with zeros
        omega = [[0] * (alpha + 1) for _ in range(alpha + 1)]
        mu = [0] * (alpha + 1)
        tau = [0] * (alpha + 1)

        lambda_idx = 0
        while lambda_idx < alpha:
            sigma = 0
            while True:
                if sigma >= alpha:
                    break
                omega[sigma + 1][lambda_idx] = omega[sigma][lambda_idx] + grid[lambda_idx][sigma]
                sigma += 1
            lambda_idx += 1

        zeta = 1
        while True:
            if zeta >= alpha:
                break

            psi = [0] * (alpha + 1)
            xi = [0] * (alpha + 1)

            chi = 0
            while True:
                if chi > alpha:
                    break

                upsilon = 0
                while upsilon <= alpha:
                    if chi > upsilon:
                        phi = omega[chi][zeta - 1] - omega[upsilon][zeta - 1]
                        val = tau[upsilon] + phi
                        if val > psi[chi]:
                            psi[chi] = val
                        if val > xi[chi]:
                            xi[chi] = val
                    else:
                        phi = omega[upsilon][zeta] - omega[chi][zeta]
                        val = mu[upsilon] + phi
                        if val > psi[chi]:
                            psi[chi] = val
                        if mu[upsilon] > xi[chi]:
                            xi[chi] = mu[upsilon]
                    upsilon += 1

                chi += 1

            mu = psi
            tau = xi

            zeta += 1

        omegA = -inf
        beta = 0
        while beta <= alpha:
            if mu[beta] > omegA:
                omegA = mu[beta]
            beta += 1

        return omegA