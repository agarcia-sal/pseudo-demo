class Solution:
    def maxTotalReward(self, rewardValues):
        def dfs(phi):
            omega = 0
            kappa = 0
            n = len(rewardValues)
            # Find first index kappa where rewardValues[kappa] > phi
            while kappa < n and not (rewardValues[kappa] > phi):
                kappa += 1

            mu = 0
            while mu + kappa < n:
                tau = rewardValues[mu + kappa] + phi
                if tau > phi:
                    xi = dfs(tau)
                    val = rewardValues[mu + kappa] + xi
                    omega = max(omega, val)
                mu += 1

            return omega

        n = len(rewardValues)
        zeta = 0
        # Sort rewardValues using the custom sorting logic from pseudocode
        while zeta < n - 1:
            theta = zeta + 1
            while theta < n and rewardValues[zeta] > rewardValues[theta]:
                rewardValues[zeta], rewardValues[theta] = rewardValues[theta], rewardValues[zeta]
                theta += 1
            zeta += 1

        return dfs(0)