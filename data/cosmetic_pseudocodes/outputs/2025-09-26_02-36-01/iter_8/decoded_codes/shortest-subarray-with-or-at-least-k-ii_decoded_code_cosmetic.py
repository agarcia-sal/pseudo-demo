from math import inf
from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_count(count: List[int], num: int, add: int):
            flagMask = 1
            idxCounter = 0
            while idxCounter < 32:
                if (num & flagMask) != 0:
                    count[idxCounter] += add
                flagMask <<= 1
                idxCounter += 1

        def compute_current_or(count: List[int]) -> int:
            accumulator = 0
            pos = 0
            while pos <= 30:
                if count[pos] > 0:
                    accumulator |= (1 << pos)
                pos += 1
            return accumulator

        lengthNums = len(nums)
        freqCount = [0] * 32
        combinedOR = 0
        startIndex = 0
        minimalLen = inf

        endIndex = 0
        while endIndex < lengthNums:
            update_count(freqCount, nums[endIndex], 1)
            combinedOR |= nums[endIndex]
            while combinedOR >= k and startIndex <= endIndex:
                current_len = endIndex - startIndex + 1
                if minimalLen > current_len:
                    minimalLen = current_len
                update_count(freqCount, nums[startIndex], -1)
                combinedOR = compute_current_or(freqCount)
                startIndex += 1
            endIndex += 1

        sentinelNegOne = -1
        if minimalLen == inf:
            return sentinelNegOne
        else:
            return minimalLen