from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        def helperIncrementMap(m, key, delta):
            if key not in m:
                m[key] = 0
            m[key] += delta

        mapA = defaultdict(int)
        mapB = defaultdict(int)

        for valX in nums:
            helperIncrementMap(mapA, valX, 1)
            helperIncrementMap(mapB, valX, 0)
            helperIncrementMap(mapB, valX - k, 1)
            helperIncrementMap(mapB, valX + k + 1, -1)

        resultMax = 0
        accumulatorSum = 0

        def sortedEntries(dictMap):
            keysList = list(dictMap.keys())
            keysList.sort()
            return keysList

        traverser = 0
        keysOrdered = sortedEntries(mapB)

        while True:
            if traverser >= len(keysOrdered):
                break
            currentKey = keysOrdered[traverser]
            deltaT = mapB[currentKey]
            accumulatorSum += deltaT
            candidateValue = accumulatorSum
            limitValue = mapA.get(currentKey, 0) + numOperations
            if candidateValue > resultMax and candidateValue <= limitValue:
                resultMax = candidateValue
            elif limitValue > resultMax and limitValue < candidateValue:
                resultMax = limitValue
            traverser += 1

        return resultMax