from collections import defaultdict

class Solution:
    def maxFrequency(self, nums, k, numOperations):
        def helperAddValue(dictMap, key, delta):
            if key not in dictMap:
                dictMap[key] = 0
            dictMap[key] += delta

        alpha = defaultdict(int)
        beta = defaultdict(int)
        idx = 0
        while idx < len(nums):
            currentElem = nums[idx]
            helperAddValue(alpha, currentElem, 1)
            helperAddValue(beta, currentElem, 0)
            helperAddValue(beta, currentElem - k, 1)
            helperAddValue(beta, currentElem + k + 1, -1)
            idx += 1

        limit = 0
        accumulator = 0
        sortedPairs = sorted(beta.items())

        def processList(arr, pos, accValue, maxValue):
            if pos == len(arr):
                return maxValue
            keyX, tVal = arr[pos]
            newAcc = accValue + tVal
            candidate = min(newAcc, alpha.get(keyX, 0) + numOperations)
            newMax = candidate if candidate > maxValue else maxValue
            return processList(arr, pos + 1, newAcc, newMax)

        limit = processList(sortedPairs, 0, accumulator, limit)
        return limit