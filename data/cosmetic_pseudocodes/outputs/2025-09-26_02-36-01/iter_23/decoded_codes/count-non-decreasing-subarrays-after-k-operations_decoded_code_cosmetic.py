class Solution:
    def countNonDecreasingSubarrays(self, nums, k):
        lengthNums = len(nums)

        def checkPermissibleRange(startIndex, count):
            aggregatedCost = 0
            peakValue = nums[startIndex]

            def innerIterator(index):
                nonlocal aggregatedCost, peakValue
                if index > count - 1:
                    return True
                else:
                    current = nums[startIndex + index]
                    if current < peakValue:
                        aggregatedCost += peakValue - current
                    peakValue = peakValue if peakValue > current else current
                    if aggregatedCost > k:
                        return False
                    else:
                        return innerIterator(index + 1)

            return innerIterator(1)

        totalPossible = (lengthNums * (lengthNums + 1)) // 2
        discardedCount = 0

        def binarySearchRange(currentStart):
            lowerBound = 1
            upperBound = lengthNums - currentStart

            def searchStep(low, high):
                if low > high:
                    return high
                midpoint = (low + high) // 2
                if checkPermissibleRange(currentStart, midpoint):
                    return searchStep(midpoint + 1, high)
                else:
                    return searchStep(low, midpoint - 1)

            return searchStep(lowerBound, upperBound)

        def loopIndex(pos):
            nonlocal discardedCount
            if pos > lengthNums - 1:
                return 0
            validRight = binarySearchRange(pos)
            discardedCount += (lengthNums - pos - validRight)
            return loopIndex(pos + 1)

        loopIndex(0)

        return totalPossible - discardedCount