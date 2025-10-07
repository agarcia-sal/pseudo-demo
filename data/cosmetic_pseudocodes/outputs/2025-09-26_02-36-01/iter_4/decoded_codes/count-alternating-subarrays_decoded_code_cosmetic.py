class Solution:
    def countAlternatingSubarrays(self, nums):
        totalCount = 0
        size = len(nums)
        if size == 0:
            return 0
        totalCount = size
        lengthSeq = 1
        index = 1
        while index < size:
            if nums[index] != nums[index - 1]:
                lengthSeq += 1
            else:
                lengthSeq = 1
            totalCount += lengthSeq - 1
            index += 1
        return totalCount