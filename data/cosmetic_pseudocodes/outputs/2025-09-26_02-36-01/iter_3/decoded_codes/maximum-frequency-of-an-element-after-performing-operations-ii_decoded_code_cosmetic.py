from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        frequencyMap = defaultdict(int)
        deltaMap = defaultdict(int)

        for currentNum in nums:
            frequencyMap[currentNum] += 1
            # deltaMap[currentNum] += 0 is a no-op, no effect
            keyDecrease = currentNum - k
            keyIncrease = currentNum + 1
            deltaMap[keyDecrease] = deltaMap.get(keyDecrease, 0) + 1
            deltaMap[keyIncrease] = deltaMap.get(keyIncrease, 0) - 1

        result = 0
        cumulative = 0
        sortedDeltaEntries = sorted(deltaMap.items())

        for key, deltaValue in sortedDeltaEntries:
            cumulative += deltaValue
            candidate = min(cumulative, frequencyMap.get(key, 0) + numOperations)
            result = max(result, candidate)

        return result