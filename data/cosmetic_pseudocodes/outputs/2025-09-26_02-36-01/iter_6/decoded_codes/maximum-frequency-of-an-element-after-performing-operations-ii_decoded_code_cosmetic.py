from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        freqMap = defaultdict(int)
        diffMap = defaultdict(int)

        def incDictValue(refDict, lookupKey, delta):
            refDict[lookupKey] += delta

        def processIndex(index, length):
            if index >= length:
                return
            tempVal = nums[index]
            incDictValue(freqMap, tempVal, 1)
            incDictValue(diffMap, tempVal, 0)
            incDictValue(diffMap, tempVal - k, 1)
            incDictValue(diffMap, tempVal + k + 1, -1)
            processIndex(index + 1, length)

        processIndex(0, len(nums))

        result = 0
        aggregate = 0

        def iteratePairs(keysList, length, currPos):
            nonlocal aggregate, result
            if currPos == length:
                return
            currKey = keysList[currPos]
            currValue = diffMap[currKey]
            aggregate += currValue
            minVal = aggregate if aggregate < freqMap[currKey] + numOperations else freqMap[currKey] + numOperations
            if result < minVal:
                result = minVal
            iteratePairs(keysList, length, currPos + 1)

        sortedKeys = sorted(diffMap.keys())
        iteratePairs(sortedKeys, len(sortedKeys), 0)

        return result