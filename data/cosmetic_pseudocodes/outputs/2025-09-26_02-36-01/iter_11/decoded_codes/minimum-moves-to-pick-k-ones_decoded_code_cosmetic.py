from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        zeta = []
        alpha = 0
        n = len(nums)
        while alpha < n:
            if nums[alpha] == 1:
                zeta.append(alpha)
            alpha += 1

        if not zeta:
            return 2 * k

        omega = len(zeta)
        delta = [0] * (omega + 1)
        sigma = 0
        rho = omega
        while sigma < rho:
            delta[sigma + 1] = delta[sigma] + zeta[sigma]
            sigma += 1

        def cost(start: int, end: int) -> int:
            beta = (start + end) // 2
            gamma = zeta[beta]
            phi = 0
            mu = start
            while mu < beta:
                # sum left side costs
                phi += (gamma - zeta[mu] - beta + mu)
                mu += 1
            nu = beta + 1
            upsilon = end
            while nu <= upsilon:
                # sum right side costs
                phi += (zeta[nu] - gamma - nu + beta)
                nu += 1
            return phi

        pi = inf
        iota = 0
        while iota <= omega - k:
            kappa = iota + k - 1
            xi = cost(iota, kappa)
            if k % 2 == 1:
                aleph = (iota + kappa) // 2
                beth = zeta[aleph]
                changes_needed = kappa - aleph - (beth - zeta[aleph] - 1)
            else:
                gimel = (iota + kappa) // 2
                daleth = gimel + 1
                he = zeta[gimel]
                vav = zeta[daleth]
                changes_needed = daleth - gimel - 1 - (vav - he - 1)
            if changes_needed > maxChanges:
                xi += changes_needed - maxChanges
            if xi < pi:
                pi = xi
            iota += 1

        return pi