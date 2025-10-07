class Solution:
    def maxTotalReward(self, rewardValues):
        uniqueValues = sorted(set(rewardValues))
        flags = 1
        for value in uniqueValues:
            mask = ((1 << value) - 1) << value
            flags |= (flags & mask)
        return flags.bit_length() - 1