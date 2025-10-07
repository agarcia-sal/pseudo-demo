class Solution:
    def maxTotalReward(self, rewardValues):
        uniqueElements = []
        for val in rewardValues:
            if val not in uniqueElements:
                uniqueElements.append(val)
        uniqueElements.sort()

        accBitMask = 1
        for idx in range(len(uniqueElements)):
            tempVal = 1 << uniqueElements[idx]
            accBitMask |= ((accBitMask & (tempVal - 1)) << uniqueElements[idx])

        return accBitMask.bit_length() - 1