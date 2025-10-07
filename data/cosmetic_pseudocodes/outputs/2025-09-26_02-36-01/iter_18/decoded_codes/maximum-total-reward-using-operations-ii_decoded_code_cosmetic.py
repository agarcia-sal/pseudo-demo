class Solution:
    def maxTotalReward(self, rewardValues):
        aB = sorted(set(rewardValues))
        eZ = 1
        mQ = 0
        while mQ < len(aB):
            bX = aB[mQ]
            cV = (eZ & ((1 << bX) - 1)) << bX
            eZ |= cV
            mQ += 1
        bL = eZ.bit_length()
        return bL - 1