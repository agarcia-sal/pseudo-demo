from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        alphaMap = defaultdict(int)
        betaMap = defaultdict(int)

        for currentVal in nums:
            alphaMap[currentVal] += 1
            betaMap[currentVal] += 0
            betaMap[currentVal - k] += 1
            betaMap[currentVal + (k + 1)] += -1

        result = 0
        cumulativeSum = 0
        keysSorted = sorted(betaMap.keys())

        for keyVal in keysSorted:
            cumulativeSum += betaMap[keyVal]
            candidate = min(cumulativeSum, alphaMap[keyVal] + numOperations)
            if candidate > result:
                result = candidate

        return result