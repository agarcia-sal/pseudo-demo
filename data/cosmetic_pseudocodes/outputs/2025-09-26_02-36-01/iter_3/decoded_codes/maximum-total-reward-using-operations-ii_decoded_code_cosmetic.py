class Solution:
    def maxTotalReward(self, rewardValues):
        uniqueValues = sorted(set(rewardValues))
        flagMask = 0b1
        index = 0
        while index < len(uniqueValues):
            value = uniqueValues[index]
            shiftedOne = 1 << value
            tempMask = flagMask & ((shiftedOne - 1) << value)
            flagMask = flagMask | tempMask
            index += 1
        return bin(flagMask).count('1') - 1