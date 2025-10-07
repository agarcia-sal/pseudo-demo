class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthNums = len(nums)

        def canMakeNonDecreasing(startIdx, segmentLen):
            adjustmentCost = 0
            maxAllowed = nums[startIdx]

            for index in range(1, segmentLen):
                currentValue = nums[startIdx + index]
                if currentValue < maxAllowed:
                    diff = maxAllowed - currentValue
                    adjustmentCost += diff
                if maxAllowed < currentValue:
                    maxAllowed = currentValue
                if adjustmentCost > k:
                    return False
            return True

        totalSubintervals = (lengthNums * (lengthNums + 1)) // 2
        invalidCount = 0

        for startIndex in range(lengthNums):
            lowerBound = 1
            upperBound = lengthNums - startIndex

            while lowerBound <= upperBound:
                midpoint = (lowerBound + upperBound) // 2
                feasible = canMakeNonDecreasing(startIndex, midpoint)

                if feasible:
                    lowerBound = midpoint + 1
                else:
                    upperBound = midpoint - 1

            invalidIntervals = (lengthNums - startIndex) - upperBound
            invalidCount += invalidIntervals

        resultCount = totalSubintervals - invalidCount
        return resultCount