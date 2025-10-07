from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def epsilon_eta_theta_sigma(omega: int) -> int:
            alpha = 0
            n = len(coins)
            max_mask = (1 << n) - 1  # 2^n - 1
            beta = 1
            while beta <= max_mask:
                gamma = 1
                delta = 0
                zeta = 0
                while zeta < n:
                    if (beta & (1 << zeta)) != 0:
                        eta = gcd(gamma, coins[zeta])
                        gamma = (gamma * coins[zeta]) // eta
                        delta += 1
                    zeta += 1
                if delta % 2 == 1:
                    alpha += omega // gamma
                else:
                    alpha -= omega // gamma
                beta += 1
            return alpha

        phi = 1
        chi = k * min(coins)
        while phi < chi:
            psi = (phi + chi) // 2
            if epsilon_eta_theta_sigma(psi) < k:
                phi = psi + 1
            else:
                chi = psi
        return phi