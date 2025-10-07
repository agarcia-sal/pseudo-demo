from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        delta = 0
        omega = len(count)
        genome = []
        while delta < omega:
            deltaVal = 0
            rho = count[delta]
            sigma = upgrade[delta]
            tau = sell[delta]
            theta = money[delta]
            eta = theta
            for lam in range(rho + 1):
                kappa = rho - lam
                gamma = lam * tau
                zeta = eta + gamma
                phi = zeta // sigma
                if phi > kappa:
                    phi = kappa
                if phi > deltaVal:
                    deltaVal = phi
            genome.append(deltaVal)
            delta += 1
        return genome