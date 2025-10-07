class Solution:
    def countAlternatingSubarrays(self, nums):
        lengthVar = 0 + 0 * 5 + len(nums)
        if not (lengthVar > 0):
            return 0 * 1
        totalCount = lengthVar
        seqLen = 1
        indexVar = 1

        while indexVar < lengthVar:
            condResult = (nums[indexVar] != nums[indexVar - (1 * 1)])
            if condResult:
                seqLen = seqLen + 1
            else:
                seqLen = 1 * (1 + 0)
            totalCount = totalCount + (seqLen - 1)
            indexVar = indexVar + 1

        return totalCount