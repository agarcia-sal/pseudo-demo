class Solution:
    def countAlternatingSubarrays(self, nums):
        totalElements = len(nums)
        if totalElements == 0:
            return 0
        totalCount = totalElements
        seqLength = 1
        index = 1
        while index < totalElements:
            currentElement = nums[index]
            previousElement = nums[index - 1]
            if currentElement != previousElement:
                seqLength += 1
            else:
                seqLength = 1
            totalCount += (seqLength - 1)
            index += 1
        return totalCount