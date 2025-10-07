class Solution:
    def maximumLength(self, nums, k):
        p = len(nums)
        # Initialize fGrid with dimensions p x (k+1), filled with 1
        fGrid = [[1] * (k + 1) for _ in range(p)]

        maxVal = 0
        outerIndex = 0

        while outerIndex < p:
            currElem = nums[outerIndex]
            hCounter = 0
            while hCounter <= k:
                innerIndex = 0
                while innerIndex < outerIndex:
                    prevElem = nums[innerIndex]
                    if currElem == prevElem:
                        candidate1 = fGrid[outerIndex][hCounter]
                        candidate2 = fGrid[innerIndex][hCounter] + 1
                        if candidate1 < candidate2:
                            fGrid[outerIndex][hCounter] = candidate2
                    else:
                        if hCounter > 0:
                            alternativeCandidate1 = fGrid[outerIndex][hCounter]
                            alternativeCandidate2 = (fGrid[innerIndex][hCounter - 1]) + 1
                            if alternativeCandidate1 < alternativeCandidate2:
                                fGrid[outerIndex][hCounter] = alternativeCandidate2
                    innerIndex += 1
                hCounter += 1

            maxCandidate = fGrid[outerIndex][k]
            if maxVal < maxCandidate:
                maxVal = maxCandidate

            outerIndex += 1

        return maxVal