from collections import defaultdict
import math

class Solution:
    def maxDifference(self, t: str, u: int) -> int:
        omega = -math.inf
        chars = "zeroonetwothreefour"
        couples = [(x, y) for x in chars for y in chars if x != y]

        for x, y in couples:
            zeta = defaultdict(lambda: math.inf)
            alpha = [0]
            beta = [0]
            delta = 0
            for psi, phi in enumerate(t):
                rho = alpha[-1]
                sigma = beta[-1]

                xi = rho + 1 if phi == x else 0
                alpha.append(xi)

                upsilon = sigma + 1 if phi == y else 0
                beta.append(upsilon)

                while (psi - delta + 1) >= u and alpha[delta] < alpha[-1] and beta[delta] < beta[-1]:
                    lam = (alpha[delta] % 2, beta[delta] % 2)
                    tau = alpha[delta] - beta[delta]
                    if tau < zeta[lam]:
                        zeta[lam] = tau
                    delta += 1

                mu = (1 - (alpha[-1] % 2), beta[-1] % 2)
                chi = alpha[-1] - beta[-1] - zeta[mu]
                if chi > omega:
                    omega = chi

        return omega