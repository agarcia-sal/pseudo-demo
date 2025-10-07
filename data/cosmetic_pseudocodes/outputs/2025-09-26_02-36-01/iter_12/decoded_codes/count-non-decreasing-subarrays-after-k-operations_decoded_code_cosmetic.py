class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthVar = len(nums)

        def verifyFeasibility(index, segmentSize):
            adjustmentCost = 0
            pivotValue = nums[index]

            iteratorCounter = 1
            while iteratorCounter < segmentSize:
                currentElement = nums[index + iteratorCounter]
                if currentElement < pivotValue:
                    adjustmentCost += pivotValue - currentElement
                if currentElement > pivotValue:
                    pivotValue = currentElement
                if adjustmentCost > k:
                    return False
                iteratorCounter += 1
            return True

        totalPossibleSubarrays = (lengthVar * (lengthVar + 1)) // 2
        invalidCount = 0

        primaryIndex = 0
        while primaryIndex < lengthVar:
            lowerBound = 1
            upperBound = lengthVar - primaryIndex

            while lowerBound <= upperBound:
                midPoint = (lowerBound + upperBound) // 2
                if verifyFeasibility(primaryIndex, midPoint):
                    lowerBound = midPoint + 1
                else:
                    upperBound = midPoint - 1

            invalidCount += (lengthVar - primaryIndex - upperBound)
            primaryIndex += 1

        return totalPossibleSubarrays - invalidCount