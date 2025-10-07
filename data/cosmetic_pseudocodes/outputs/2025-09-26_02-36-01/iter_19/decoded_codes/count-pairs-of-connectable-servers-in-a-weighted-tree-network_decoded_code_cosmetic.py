from collections import defaultdict
from typing import List, Tuple

class Solution:
    def countPairsOfConnectableServers(self, edges: List[Tuple[int, int, int]], signalSpeed: int) -> List[int]:
        alpha = defaultdict(list)
        for x, y, z in edges:
            alpha[x].append((y, z))
            alpha[y].append((x, z))

        omega = len(alpha)
        sigma = [0] * omega

        def dfs(epsilon: int, delta: int, gamma: int, theta: List[int]) -> int:
            if gamma % signalSpeed == 0:
                theta.append(epsilon)
            phi = 0
            for iota, kappa in alpha[epsilon]:
                if iota != delta:
                    phi += dfs(iota, epsilon, gamma + kappa, theta)
            return phi + 1 if gamma % signalSpeed == 0 else phi

        def count_pairs_through_c(lambda_: int) -> int:
            chi = []
            for mu, nu in alpha[lambda_]:
                psi = []
                dfs(mu, lambda_, nu, psi)
                chi.append(psi)
            tau = 0
            rho = len(chi)
            for xi in range(rho - 1):
                for upsilon in range(xi + 1, rho):
                    tau += len(chi[xi]) * len(chi[upsilon])
            return tau

        for zeta in range(omega):
            sigma[zeta] = count_pairs_through_c(zeta)

        return sigma