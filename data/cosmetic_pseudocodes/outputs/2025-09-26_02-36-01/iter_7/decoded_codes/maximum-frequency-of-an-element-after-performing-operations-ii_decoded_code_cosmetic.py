from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        def getDefaultInt():
            return 0

        frequencyMap = defaultdict(getDefaultInt)
        deltaMap = defaultdict(getDefaultInt)

        idx = 0
        while idx < len(nums):
            currentNum = nums[idx]
            frequencyMap[currentNum] += 1
            deltaMap[currentNum] += 0
            deltaMap[currentNum - k] += 1
            deltaMap[currentNum + k + 1] += -1
            idx += 1

        maximumFrequency = 0
        cumulativeSum = 0
        pairsList = [(key, deltaMap[key]) for key in deltaMap]
        sortedPairs = sorted(pairsList, key=lambda x: x[0])

        def loopRecursor(currentIndex, cumulativeSumInner, maxFreqInner):
            if currentIndex >= len(sortedPairs):
                return maxFreqInner
            keyToUse, valueIncrement = sortedPairs[currentIndex]
            newCumulativeSum = cumulativeSumInner + valueIncrement
            candidate1 = maxFreqInner
            candidate2 = min(newCumulativeSum, frequencyMap.get(keyToUse, 0) + numOperations)
            newMaxFreq = max(candidate1, candidate2)
            return loopRecursor(currentIndex + 1, newCumulativeSum, newMaxFreq)

        return loopRecursor(0, cumulativeSum, maximumFrequency)