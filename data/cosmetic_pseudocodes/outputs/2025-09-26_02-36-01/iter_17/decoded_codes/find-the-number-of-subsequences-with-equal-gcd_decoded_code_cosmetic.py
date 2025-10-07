from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        modValue = 10**9 + 7
        topVal = max(nums) if nums else 0
        countMatrix = [[0] * (topVal + 1) for _ in range(topVal + 1)]
        countMatrix[0][0] = 1

        for currentVal in nums:
            tempMatrix = [[0] * (topVal + 1) for _ in range(topVal + 1)]

            for outerIndex in range(topVal + 1):
                for innerIndex in range(topVal + 1):
                    prevCount = countMatrix[outerIndex][innerIndex]
                    if prevCount == 0:
                        continue

                    # Add previous count without changes
                    tempMatrix[outerIndex][innerIndex] = (tempMatrix[outerIndex][innerIndex] + prevCount) % modValue

                    gcdX = gcd(outerIndex, currentVal)
                    tempMatrix[gcdX][innerIndex] = (tempMatrix[gcdX][innerIndex] + prevCount) % modValue

                    gcdY = gcd(innerIndex, currentVal)
                    tempMatrix[outerIndex][gcdY] = (tempMatrix[outerIndex][gcdY] + prevCount) % modValue

            countMatrix = tempMatrix

        aggregate = 0
        for gIndex in range(1, topVal + 1):
            aggregate = (aggregate + countMatrix[gIndex][gIndex]) % modValue

        return aggregate