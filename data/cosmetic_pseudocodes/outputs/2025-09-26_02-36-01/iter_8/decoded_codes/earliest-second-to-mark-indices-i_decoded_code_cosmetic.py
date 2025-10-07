class Solution:
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        lengthNums = len(nums)
        lengthChanges = len(changeIndices)

        def can_mark_by_second(k):
            lastPos = [-1] * lengthNums  # Initialize lastPos with -1
            iteratorIndex = 0

            # Update lastPos with the latest iteratorIndex of each changed index up to k
            while iteratorIndex < k:
                changeIndexCurrent = changeIndices[iteratorIndex] - 1
                lastPos[changeIndexCurrent] = iteratorIndex
                iteratorIndex += 1

            totalDecrements = sum(nums)
            availableUnits = 0
            markedSet = set()

            scanIndex = 0
            while scanIndex < k:
                currIndex = changeIndices[scanIndex] - 1

                if currIndex not in markedSet:
                    if lastPos[currIndex] == scanIndex:
                        if nums[currIndex] <= availableUnits:
                            availableUnits -= nums[currIndex]
                            markedSet.add(currIndex)
                        else:
                            return False
                    else:
                        availableUnits += 1
                else:
                    availableUnits += 1

                scanIndex += 1

            return len(markedSet) == lengthNums

        lowerBound = 0
        upperBound = lengthChanges + 1

        while lowerBound < upperBound:
            middle = (lowerBound + upperBound) // 2
            if can_mark_by_second(middle):
                upperBound = middle
            else:
                lowerBound += 1

        if lowerBound <= lengthChanges:
            return lowerBound
        else:
            return -1