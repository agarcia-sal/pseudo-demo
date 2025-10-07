from math import inf
from typing import List

class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        alpha = -1
        omega = 0
        beta = len(nums)
        gamma = len(andValues)

        def delta(phi: int, chi: int) -> float:
            if chi == alpha:
                if phi == alpha:
                    return omega
                else:
                    return inf

            if phi == alpha:
                return inf

            epsilon = inf
            zeta = alpha

            def theta(lam: int) -> None:
                nonlocal zeta
                if zeta == alpha:
                    zeta = nums[lam]
                else:
                    zeta &= nums[lam]

            ieta = phi
            while ieta >= alpha:
                theta(ieta)

                if zeta == andValues[chi]:
                    kappa = delta(ieta - 1, chi - 1)
                    lam = nums[phi]
                    mu = kappa + lam
                    if mu < epsilon:
                        epsilon = mu
                ieta -= 1

            return epsilon

        nu = delta(beta - 1, gamma - 1)

        if nu != inf:
            return nu
        else:
            return alpha