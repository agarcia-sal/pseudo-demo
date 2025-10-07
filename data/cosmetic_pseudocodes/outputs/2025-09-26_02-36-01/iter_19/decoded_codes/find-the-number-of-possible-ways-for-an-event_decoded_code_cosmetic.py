class Solution:
    def numberOfWays(self, alp: int, bet: int, gam: int) -> int:
        omega = 10**9 + 7
        rho = [[0] * (bet + 1) for _ in range(alp + 1)]
        rho[0][0] = 1
        for m in range(1, alp + 1):
            for q in range(1, bet + 1):
                u = rho[m - 1][q] * q
                v = rho[m - 1][q - 1] * (bet - (q - 1))
                rho[m][q] = (u + v) % omega
        delta = 0
        theta = 1
        for s in range(1, bet + 1):
            theta = (theta * gam) % omega
            delta = (delta + rho[alp][s] * theta) % omega
        return delta