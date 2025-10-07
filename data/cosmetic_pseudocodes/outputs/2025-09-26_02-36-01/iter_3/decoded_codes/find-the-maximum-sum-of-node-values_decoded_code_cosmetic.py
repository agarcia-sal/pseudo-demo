class Solution:
    def maximumValueSum(self, nums, k):
        aggregateSum = 0
        positiveGainCount = 0
        smallestGain = float('inf')

        for currentNum in nums:
            xorResult = currentNum ^ k
            netGain = xorResult - currentNum

            if netGain > 0:
                positiveGainCount += 1

            maxVal = currentNum if currentNum >= xorResult else xorResult
            aggregateSum += maxVal

            absGain = abs(netGain)
            if absGain < smallestGain:
                smallestGain = absGain

        if positiveGainCount % 2 != 0:
            aggregateSum -= smallestGain

        return aggregateSum