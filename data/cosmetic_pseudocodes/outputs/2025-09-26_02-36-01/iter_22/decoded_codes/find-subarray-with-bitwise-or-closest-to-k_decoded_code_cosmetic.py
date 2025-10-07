class Solution:
    def minimumDifference(self, nums, k):
        length = len(nums)
        bestDiff = float('inf')
        for outerIndex in range(length):
            runningOr = 0
            for innerIndex in range(outerIndex, length):
                runningOr |= nums[innerIndex]
                currentDiff = abs(k - runningOr)
                if currentDiff < bestDiff:
                    bestDiff = currentDiff
                if bestDiff == 0:
                    return 0
        return bestDiff