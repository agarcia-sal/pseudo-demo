class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthNums = len(nums)

        def isValidWindow(beginIdx, winLen):
            penaltyAccumulator = 0
            maximumSoFar = nums[beginIdx]

            def iterate(currentStep, limit):
                nonlocal penaltyAccumulator, maximumSoFar
                if currentStep == limit:
                    return

                currentVal = nums[beginIdx + currentStep]
                if currentVal < maximumSoFar:
                    penaltyAccumulator += maximumSoFar - currentVal

                if penaltyAccumulator > k:
                    raise RuntimeError("earlyStop")

                if currentVal > maximumSoFar:
                    maximumSoFar = currentVal

                iterate(currentStep + 1, limit)

            try:
                iterate(1, winLen)
            except RuntimeError as e:
                if str(e) == "earlyStop":
                    return False
                raise
            return True

        totalSubarrays = lengthNums * (lengthNums + 1) // 2
        countInvalid = 0

        for startIdx in range(lengthNums):
            lowBound = 1
            upBound = lengthNums - startIdx

            while lowBound <= upBound:
                midpoint = (lowBound + upBound) // 2
                if isValidWindow(startIdx, midpoint):
                    lowBound = midpoint + 1
                else:
                    upBound = midpoint - 1

            countInvalid += lengthNums - startIdx - upBound

        return totalSubarrays - countInvalid