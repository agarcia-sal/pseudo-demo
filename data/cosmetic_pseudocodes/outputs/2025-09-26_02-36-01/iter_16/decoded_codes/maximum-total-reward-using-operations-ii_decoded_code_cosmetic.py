class Solution:
    def maxTotalReward(self, rewardValues):
        alpha = set()
        for val in rewardValues:
            if val not in alpha:
                alpha.add(val)
        beta = 1
        gammaList = list(alpha)
        idx = 0
        while idx < len(gammaList):
            delta = gammaList[idx]
            epsilon = (1 << delta) - 1
            beta |= ((beta & epsilon) << delta)
            idx += 1
        zeta = 0
        eta = beta
        while eta > 0:
            eta >>= 1
            zeta += 1
        return zeta - 1