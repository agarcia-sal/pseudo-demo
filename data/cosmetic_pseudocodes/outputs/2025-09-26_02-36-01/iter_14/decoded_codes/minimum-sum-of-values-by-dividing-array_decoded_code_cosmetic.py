from math import inf
from functools import lru_cache

class Solution:
    def minimumValueSum(self, nums, andValues):
        omega = len(nums)
        sigma = len(andValues)

        @lru_cache(None)
        def delta(alpha, beta):
            if beta == -1:
                return 0 if alpha == -1 else inf
            if alpha == -1:
                return inf

            psi = inf
            rho = -1
            gamma = alpha
            while gamma >= -1:
                if rho == -1:
                    if gamma == -1:
                        break  # avoid index error for nums[-1]
                    rho = nums[gamma]
                else:
                    if gamma == -1:
                        break
                    rho &= nums[gamma]

                if rho == andValues[beta]:
                    cand = delta(gamma - 1, beta - 1) + nums[alpha]
                    if cand < psi:
                        psi = cand
                gamma -= 1

            return psi

        outcome = delta(omega - 1, sigma - 1)
        return outcome if outcome != inf else -1