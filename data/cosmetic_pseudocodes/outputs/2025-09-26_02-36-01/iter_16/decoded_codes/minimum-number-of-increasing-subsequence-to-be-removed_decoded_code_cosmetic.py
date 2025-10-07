from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        epsilon = 0
        omega = 1
        beta = len(nums)
        if not (beta > epsilon):
            return epsilon
        zeta = [omega] * beta
        phi = omega
        while phi < beta:
            psi = epsilon
            while psi < phi:
                if not (nums[phi] > nums[psi]):
                    if zeta[phi] < (zeta[psi] + omega):
                        zeta[phi] = zeta[psi] + omega
                psi += omega
            phi += omega
        sigma = zeta[0]
        delta = omega
        while delta < beta:
            if sigma < zeta[delta]:
                sigma = zeta[delta]
            delta += omega
        return sigma