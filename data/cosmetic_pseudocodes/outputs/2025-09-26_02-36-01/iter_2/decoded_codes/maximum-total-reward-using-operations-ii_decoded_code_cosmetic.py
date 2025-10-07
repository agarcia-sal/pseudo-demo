class Solution:
    def maxTotalReward(self, rewardValues):
        uniqueNumbers = sorted(set(rewardValues))
        flag = 1
        index = 0
        while index < len(uniqueNumbers):
            currentValue = uniqueNumbers[index]
            bitMask = ((1 << currentValue) - 1) << currentValue
            flag = flag | (flag & bitMask)
            index += 1
        return flag.bit_length() - 1