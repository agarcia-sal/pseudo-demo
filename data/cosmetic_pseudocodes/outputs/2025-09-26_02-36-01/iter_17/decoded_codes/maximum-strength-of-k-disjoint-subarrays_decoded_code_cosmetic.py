from math import inf
from typing import List

class Solution:
    def maximumStrength(self, nums: List[int], k: int) -> int:
        lengthVar = len(nums)
        storageTable = [[-inf] * (k + 1) for _ in range(lengthVar + 1)]
        storageTable[0][0] = 0

        outerIndex = 1
        while outerIndex <= lengthVar:
            innerIndex = 1
            while innerIndex <= k:
                accumulator = 0
                reverseIndex = outerIndex
                while reverseIndex > 0:
                    accumulator += nums[reverseIndex - 1]

                    # Calculate factor depending on parity of innerIndex
                    if innerIndex % 2 == 1:
                        factor = (k - innerIndex)
                    else:
                        factor = - (k - innerIndex)

                    prevVal = storageTable[reverseIndex - 1][innerIndex - 1] + factor * accumulator
                    if storageTable[outerIndex][innerIndex] < prevVal:
                        storageTable[outerIndex][innerIndex] = prevVal
                    reverseIndex -= 1

                if storageTable[outerIndex][innerIndex] < storageTable[outerIndex - 1][innerIndex]:
                    storageTable[outerIndex][innerIndex] = storageTable[outerIndex - 1][innerIndex]

                innerIndex += 1
            outerIndex += 1

        return storageTable[lengthVar][k]