class Solution:
    def maxTotalReward(self, rewardValues):
        uniqueNumbers = sorted(set(rewardValues))
        accumulator = 1
        index = 0
        while index < len(uniqueNumbers):
            currentValue = uniqueNumbers[index]
            shiftedOne = 1 << currentValue
            combinedMask = accumulator & (shiftedOne - 1)
            updatedMask = combinedMask << currentValue
            accumulator |= updatedMask
            index += 1
        resultLength = accumulator.bit_length()
        return resultLength - 1