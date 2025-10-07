from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalElems = len(nums)
        resultCounter = 0
        outerIndex = 0
        while outerIndex <= totalElems - 1:
            andAccumulator = nums[outerIndex]
            innerIndex = outerIndex
            while innerIndex < totalElems:
                andAccumulator &= nums[innerIndex]
                if andAccumulator == k:
                    resultCounter += 1
                if andAccumulator < k:
                    break
                innerIndex += 1
            outerIndex += 1
        return resultCounter