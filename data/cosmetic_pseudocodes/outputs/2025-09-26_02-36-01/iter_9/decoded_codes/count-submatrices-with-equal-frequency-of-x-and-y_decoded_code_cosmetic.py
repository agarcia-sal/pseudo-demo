from typing import List

class Solution:
    def numberOfSubmatrices(self, omega: List[List[str]]) -> int:
        if not omega or not omega[0]:
            return 0

        alpha = len(omega)
        beta = len(omega[0])

        # Initialize gamma with dimensions (alpha+2) x (beta+2), each element is [0,0]
        gamma = [[[0, 0] for _ in range(beta + 2)] for _ in range(alpha + 2)]

        delta = 1
        while delta <= alpha:
            epsilon = 1
            while epsilon <= beta:
                zeta_0, zeta_1 = gamma[delta - 1][epsilon]
                eta_0, eta_1 = gamma[delta][epsilon - 1]
                theta_0, theta_1 = gamma[delta - 1][epsilon - 1]

                gamma[delta][epsilon][0] = (zeta_0 + eta_0) - theta_0
                gamma[delta][epsilon][1] = (zeta_1 + eta_1) - theta_1

                i_pos = delta - 1
                j_pos = epsilon - 1
                val = omega[i_pos][j_pos]

                if val == 'X':
                    gamma[delta][epsilon][0] += 1
                elif val == 'Y':
                    gamma[delta][epsilon][1] += 1

                epsilon += 1
            delta += 1

        sigma = 0
        for mu in range(1, alpha + 1):
            for nu in range(1, beta + 1):
                phi, chi = gamma[mu][nu]
                if phi > 0 and phi == chi:
                    sigma += 1

        return sigma