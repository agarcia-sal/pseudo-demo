class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthNums = len(nums)

        def validateNonDecreasingSegment(pos, segLen):
            penalty = 0
            peakValue = nums[pos]
            step = 1
            while True:
                if step == segLen:
                    break
                currentVal = nums[pos + step]
                if currentVal < peakValue:
                    penalty += peakValue - currentVal
                if currentVal > peakValue:
                    peakValue = currentVal
                if penalty > k:
                    return False
                step += 1
            return True

        totalCount = lengthNums * (lengthNums + 1) // 2
        countInvalid = 0

        outerIndex = 0
        while outerIndex < lengthNums:
            lowBound = 1
            upBound = lengthNums - outerIndex
            while lowBound <= upBound:
                middle = (lowBound + upBound) // 2
                if validateNonDecreasingSegment(outerIndex, middle):
                    lowBound = middle + 1
                else:
                    upBound = middle - 1
            incrementValue = (lengthNums - outerIndex - upBound)
            countInvalid += incrementValue
            outerIndex += 1

        resultCount = totalCount - countInvalid
        return resultCount