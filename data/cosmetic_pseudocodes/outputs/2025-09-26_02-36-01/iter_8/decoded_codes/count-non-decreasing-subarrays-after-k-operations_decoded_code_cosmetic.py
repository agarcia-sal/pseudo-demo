from math import floor

class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthOfNums = len(nums)

        def canMakeNonDecreasing(startIndex, segmentLength):
            accumulatedCost = 0
            runningMax = nums[startIndex]
            indexOffset = 1
            while indexOffset < segmentLength:
                currentValue = nums[startIndex + indexOffset]
                if currentValue < runningMax:
                    accumulatedCost += runningMax - currentValue
                else:
                    runningMax = currentValue
                if accumulatedCost > k:
                    return False
                indexOffset += 1
            return True

        totalPossibleSubarrays = lengthOfNums * (lengthOfNums + 1) // 2
        countInvalid = 0

        outerIndex = 0
        while outerIndex < lengthOfNums:
            minimumLength = 1
            maximumLength = lengthOfNums - outerIndex

            while minimumLength <= maximumLength:
                midLength = (minimumLength + maximumLength) // 2
                if canMakeNonDecreasing(outerIndex, midLength):
                    minimumLength = midLength + 1
                else:
                    maximumLength = midLength - 1

            decrementToAdd = (lengthOfNums - outerIndex) - maximumLength
            countInvalid += decrementToAdd
            outerIndex += 1

        resultSubarrays = totalPossibleSubarrays - countInvalid
        return resultSubarrays