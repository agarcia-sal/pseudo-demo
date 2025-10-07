from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        lengthVar = len(nums)
        dpArray = [0] * lengthVar

        outerIndex = lengthVar - 2
        while outerIndex >= 0:
            currentMax = 0
            innerIndex = outerIndex + 1
            while innerIndex <= lengthVar - 1:
                computedScore = (innerIndex - outerIndex) * nums[innerIndex]
                combinedScore = computedScore + dpArray[innerIndex]
                if currentMax < combinedScore:
                    currentMax = combinedScore
                innerIndex += 1
            dpArray[outerIndex] = currentMax
            outerIndex -= 1

        return dpArray[0]