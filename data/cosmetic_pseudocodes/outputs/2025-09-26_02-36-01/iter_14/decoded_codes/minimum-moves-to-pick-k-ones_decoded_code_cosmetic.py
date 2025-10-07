from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        beta = [i for i, val in enumerate(nums) if val == 1]

        if not beta:
            return k * 2

        omega = len(beta)
        sigma = [0] * (omega + 1)
        for delta in range(omega):
            sigma[delta + 1] = sigma[delta] + beta[delta]

        def cost(start: int, end: int) -> int:
            mu = (start + end) // 2
            pi = beta[mu]
            lambda_ = 0

            for epsilon in range(start, mu):
                lambda_ += pi - beta[epsilon] - (mu - epsilon)
            for zeta in range(mu + 1, end + 1):
                lambda_ += beta[zeta] - pi - (zeta - mu)
            return lambda_

        theta = inf

        for alpha in range(omega - k + 1):
            psi = alpha + k - 1
            rho = cost(alpha, psi)

            if k % 2 == 1:
                mu = (alpha + psi) // 2
                pi = beta[mu]
                xi = psi - mu - (pi - beta[mu] - 1)
            else:
                left_mu = (alpha + psi) // 2
                right_mu = left_mu + 1
                left_pi = beta[left_mu]
                right_pi = beta[right_mu]
                xi = right_mu - left_mu - 1 - (right_pi - left_pi - 1)

            if xi > maxChanges:
                rho += xi - maxChanges

            if rho < theta:
                theta = rho

        return theta