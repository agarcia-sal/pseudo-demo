class Solution:
    def maximumValueSum(self, nums: list[int], k: int) -> int:
        cumulativeTotal = 0
        positiveGainsCounter = 0
        smallestGain = float('inf')

        for currentNumber in nums:
            computedXor = currentNumber ^ k
            computedGain = computedXor - currentNumber

            if computedGain > 0:
                positiveGainsCounter += 1

            if currentNumber > computedXor:
                cumulativeTotal += currentNumber
            else:
                cumulativeTotal += computedXor

            absGain = abs(computedGain)
            if smallestGain > absGain:
                smallestGain = absGain

        if positiveGainsCounter % 2 == 1:
            cumulativeTotal -= smallestGain

        return cumulativeTotal