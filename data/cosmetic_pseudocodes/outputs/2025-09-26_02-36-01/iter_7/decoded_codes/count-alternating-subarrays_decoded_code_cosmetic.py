class Solution:
    def countAlternatingSubarrays(self, nums):
        totalCount = 0
        size = len(nums)
        if size == 0:
            return 0
        totalCount = size
        seqLen = 1
        index = 1
        while index <= size - 1:
            if nums[index] != nums[index - 1]:
                seqLen += 1
            else:
                seqLen = 1
            totalCount += seqLen - 1
            index += 1
        return totalCount