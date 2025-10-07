from functools import lru_cache

class Solution:

    def maxTotalReward(self, rewardValues):
        rewardValues.sort()

        @lru_cache(None)
        def dfs(zeta):
            omega = 0
            tau = 0
            n = len(rewardValues)
            # Find the first index tau where rewardValues[tau] > zeta
            while tau < n and rewardValues[tau] <= zeta:
                tau += 1

            for psi in range(n - tau):
                upsilon = rewardValues[tau + psi]
                # Since upsilon > zeta, zeta + upsilon > zeta always holds (check aligned with pseudo)
                total = upsilon + dfs(zeta + upsilon)
                if omega < total:
                    omega = total
            return omega

        return dfs(0)