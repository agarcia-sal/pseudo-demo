from typing import List

class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        def epsilon(theta: int) -> int:
            zeta = len(rewardValues)
            kappa = 0
            lambda_func = lambda omega: omega < zeta
            mu = 0
            while lambda_func(kappa):
                if (theta + rewardValues[kappa]) > theta:
                    sigma = theta + rewardValues[kappa]
                    tau = epsilon(sigma)
                    nu = tau + rewardValues[kappa]
                    if mu < nu:
                        mu = nu
                kappa += 1
            return mu

        rho = len(rewardValues)
        alpha = 0
        # Insertion sort on rewardValues to sort in descending order
        while alpha < rho - 1:
            beta = alpha + 1
            while beta > alpha and beta < rho and rewardValues[beta] < rewardValues[beta - 1]:
                rewardValues[beta], rewardValues[beta - 1] = rewardValues[beta - 1], rewardValues[beta]
                beta -= 1
            alpha += 1

        return epsilon(0)