class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        lengthNums = len(nums)

        def canMakeNonDecreasing(startIdx: int, lenSegment: int) -> bool:
            adjustmentCost = 0
            maxVal = nums[startIdx]

            for indexCounter in range(1, lenSegment):
                currentVal = nums[startIdx + indexCounter]
                if currentVal < maxVal:
                    adjustmentCost += maxVal - currentVal
                else:
                    maxVal = currentVal
                if adjustmentCost > k:
                    return False
            return True

        allSubarraysCount = lengthNums * (lengthNums + 1) // 2
        excludedSubarraysCount = 0

        for outerIdx in range(lengthNums):
            lowBound, highBound = 1, lengthNums - outerIdx
            while lowBound <= highBound:
                middle = (lowBound + highBound) // 2
                if canMakeNonDecreasing(outerIdx, middle):
                    lowBound = middle + 1
                else:
                    highBound = middle - 1
            excludedSubarraysCount += lengthNums - outerIdx - highBound

        return allSubarraysCount - excludedSubarraysCount