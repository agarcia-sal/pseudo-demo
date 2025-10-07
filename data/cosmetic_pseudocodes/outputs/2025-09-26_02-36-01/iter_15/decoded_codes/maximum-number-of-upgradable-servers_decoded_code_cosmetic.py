from typing import List

class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        beta = []
        for theta in range(len(count)):
            xi = count[theta]
            rho = upgrade[theta]
            psi = sell[theta]
            omega = money[theta]

            delta = 0
            tau = omega
            for phi in range(xi + 1):
                sigma = xi - phi
                upsold = phi
                acumulated = tau + upsold * psi
                presale = acumulated
                purchasable = presale // rho
                if purchasable > sigma:
                    purchasable = sigma
                if delta < purchasable:
                    delta = purchasable
            beta.append(delta)
        return beta