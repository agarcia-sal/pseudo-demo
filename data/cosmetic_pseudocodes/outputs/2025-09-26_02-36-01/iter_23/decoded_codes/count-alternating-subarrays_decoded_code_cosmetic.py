class Solution:
    def countAlternatingSubarrays(self, nums):
        totalElements = len(nums)
        if totalElements == 0:
            return 0
        result = totalElements
        sequenceLength = 1

        def recur(j):
            nonlocal result, sequenceLength
            if j >= totalElements:
                return
            if nums[j] != nums[j - 1]:
                sequenceLength += 1
            else:
                sequenceLength = 1
            result += sequenceLength - 1
            recur(j + 1)

        recur(1)
        return result