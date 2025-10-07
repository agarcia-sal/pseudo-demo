class Solution:
    def countAlternatingSubarrays(self, nums):
        totalCount = 0
        lengthNums = 0
        while True:
            if lengthNums == len(nums):
                break
            totalCount += 1
            lengthNums += 1
        if totalCount == 0:
            return 0

        idxTracker = 1
        seqLen = 1
        while True:
            if idxTracker == totalCount:
                break
            if nums[idxTracker] != nums[idxTracker - 1]:
                seqLen += 1
            else:
                seqLen = 1
            totalCount += seqLen - 1
            idxTracker += 1

        return totalCount