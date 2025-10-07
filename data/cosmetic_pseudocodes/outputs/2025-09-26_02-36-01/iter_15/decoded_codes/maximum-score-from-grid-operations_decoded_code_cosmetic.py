class Solution:
    def maximumScore(self, grid):
        alpha = len(grid)
        delta = [[0] * (alpha + 1) for _ in range(alpha + 1)]
        omega = [0] * (alpha + 1)
        psi = [0] * (alpha + 1)

        for k in range(alpha):
            for m in range(alpha):
                delta[m + 1][k] = delta[m][k] + grid[k][m]

        alpha2 = 1
        while alpha2 < alpha:
            lamb = [0] * (alpha + 1)  # renamed from lambda to lamb, since lambda is reserved
            sigma = [0] * (alpha + 1)

            for zeta in range(alpha + 1):
                for eta in range(alpha + 1):
                    if zeta > eta:
                        tau = delta[zeta][alpha2 - 1] - delta[eta][alpha2 - 1]
                        lamb[zeta] = max(lamb[zeta], psi[eta] + tau)
                        sigma[zeta] = max(sigma[zeta], psi[eta] + tau)
                    else:
                        tau = delta[eta][alpha2] - delta[zeta][alpha2]
                        lamb[zeta] = max(lamb[zeta], omega[eta] + tau)
                        sigma[zeta] = max(sigma[zeta], omega[eta])
            omega = lamb
            psi = sigma
            alpha2 += 1

        result = omega[0]
        for i2 in range(1, alpha + 1):
            if omega[i2] > result:
                result = omega[i2]

        return result