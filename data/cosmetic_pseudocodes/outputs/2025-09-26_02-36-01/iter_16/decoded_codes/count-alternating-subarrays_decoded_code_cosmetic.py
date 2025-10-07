class Solution:
    def countAlternatingSubarrays(self, nums):
        lengthTracker = len(nums)
        if lengthTracker == 0:
            return 0
        totalCounter = lengthTracker
        sequenceMeasure = 1
        indexCounter = 1
        while indexCounter < lengthTracker:
            if nums[indexCounter] != nums[indexCounter - 1]:
                sequenceMeasure += 1
            else:
                sequenceMeasure = 1
            totalCounter += (sequenceMeasure - 1)
            indexCounter += 1
        return totalCounter