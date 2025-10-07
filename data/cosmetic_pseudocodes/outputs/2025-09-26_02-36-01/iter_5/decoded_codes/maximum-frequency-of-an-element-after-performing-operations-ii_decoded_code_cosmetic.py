from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        frequencyMap = defaultdict(int)
        deltaMap = defaultdict(int)

        def processIndex(i: int) -> None:
            if i >= len(nums):
                return
            currentNum = nums[i]
            frequencyMap[currentNum] += 1
            deltaMap[currentNum] += 0
            deltaMap[currentNum - k] += 1
            deltaMap[currentNum + k + 1] += -1
            processIndex(i + 1)

        processIndex(0)

        maxFreq = 0
        cumulativeSum = 0
        sortedDeltas = sorted(deltaMap.items(), key=lambda x: x[0])

        def iterateDeltas(j: int) -> None:
            nonlocal cumulativeSum, maxFreq
            if j >= len(sortedDeltas):
                return
            keyToUse, deltaValue = sortedDeltas[j]
            cumulativeSum += deltaValue
            candidateValue = min(cumulativeSum, frequencyMap[keyToUse] + numOperations)
            if candidateValue > maxFreq:
                maxFreq = candidateValue
            iterateDeltas(j + 1)

        iterateDeltas(0)

        return maxFreq