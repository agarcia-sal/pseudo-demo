from math import floor
from typing import List, Tuple

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[Tuple[int, int]]) -> List[int]:
        zeta = len(s)
        delta = [0] * (zeta + 1)  # prefix counts of '0's
        omega = [0] * (zeta + 1)  # prefix counts of '1's

        for iota in range(zeta):
            delta[iota + 1] = delta[iota] + (1 if s[iota] == '0' else 0)
            omega[iota + 1] = omega[iota] + (1 if s[iota] == '1' else 0)

        def count_valid_substrings(alpha: int, beta: int) -> int:
            gamma = 0
            phi = alpha
            while phi <= beta:
                mu = phi
                nu = beta + 1
                while mu < nu:
                    xi = (mu + nu) // 2
                    sigma = delta[xi + 1] - delta[phi]
                    tau = omega[xi + 1] - omega[phi]
                    if sigma <= k or tau <= k:
                        mu = xi + 1
                    else:
                        nu = xi
                psi = mu - 1
                if psi >= phi:
                    gamma += (psi - phi + 1)
                phi += 1
            return gamma

        rho = []
        for lam, omicron in queries:
            rho.append(count_valid_substrings(lam, omicron))

        return rho