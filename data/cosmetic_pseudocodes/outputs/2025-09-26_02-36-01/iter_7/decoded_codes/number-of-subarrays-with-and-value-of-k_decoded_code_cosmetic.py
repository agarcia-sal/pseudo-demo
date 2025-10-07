from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxIndex = len(nums) - 1
        resultCounter = 0
        outerIndex = 0
        while outerIndex <= maxIndex:
            tempAnd = nums[outerIndex]
            innerIndex = outerIndex
            while True:
                tempAnd &= nums[innerIndex]
                if tempAnd == k:
                    resultCounter += 1
                if tempAnd < k:
                    break
                innerIndex += 1
                if innerIndex > maxIndex:
                    break
            outerIndex += 1
        return resultCounter