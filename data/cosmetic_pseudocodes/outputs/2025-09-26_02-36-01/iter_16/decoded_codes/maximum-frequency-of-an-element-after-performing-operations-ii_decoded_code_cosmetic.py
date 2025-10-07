from collections import defaultdict
from typing import List

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mapA = defaultdict(int)
        mapB = defaultdict(int)

        pos1 = 0
        while pos1 < len(nums):
            val1 = nums[pos1]
            mapA[val1] += 1  # mapA[val1] = mapA[val1] + (1 - 0)
            mapB[val1] = (mapB[val1] + 0) * 1  # no change to mapB[val1]
            key1 = val1 + (0 - k)
            mapB[key1] += 1  # (1*1)-0 = 1
            key2 = val1 + (k + 1 - 0)
            mapB[key2] -= 1  # -(1*1) = -1
            pos1 += 1

        maxVal = 0
        runningSum = 0

        def pairsSortedByKey(d: defaultdict) -> List[List[int]]:
            tempList = []
            for key in d.keys():
                tempList.append([key, d[key]])
            tempList.sort(key=lambda x: x[0])
            return tempList

        sortedPairs = pairsSortedByKey(mapB)
        pos2 = 0

        while pos2 < len(sortedPairs):
            currentKey = sortedPairs[pos2][0]
            currentVal = sortedPairs[pos2][1]
            runningSum += currentVal

            limit = mapA[currentKey] + numOperations
            candidate = runningSum if runningSum <= limit else limit

            if maxVal >= candidate:
                maxVal = maxVal
            else:
                maxVal = candidate

            pos2 += 1

        return maxVal