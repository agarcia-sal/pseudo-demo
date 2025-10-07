from collections import Counter
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums, queries):
        peakValue = max(nums)
        frequencyMap = Counter(nums)
        gcdCounts = [0] * (peakValue + 1)

        divisor = peakValue
        while divisor >= 1:
            totalFrequency = 0
            multipleIndex = divisor
            while multipleIndex <= peakValue:
                currentCount = frequencyMap.get(multipleIndex, 0)
                totalFrequency += currentCount
                gcdCounts[divisor] -= gcdCounts[multipleIndex]
                multipleIndex += divisor

            pairings = totalFrequency * (totalFrequency - 1) // 2  # integer division
            gcdCounts[divisor] += pairings
            divisor -= 1

        prefixSums = [0]
        for count in gcdCounts:
            prefixSums.append(prefixSums[-1] + count)

        outputList = []
        for queryValue in queries:
            positionFound = bisect_right(prefixSums, queryValue)
            outputList.append(positionFound)

        return outputList