class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        lengthNums = len(nums)
        lengthPattern = len(pattern)
        tally = 0
        outerIndex = 0
        while outerIndex <= lengthNums - lengthPattern - 1:
            isMatch = True
            innerPosition = 0
            while innerPosition < lengthPattern:
                currentPatternValue = pattern[innerPosition]
                valA = nums[outerIndex + innerPosition]
                valB = nums[outerIndex + innerPosition + 1]
                if currentPatternValue == 1 and valB <= valA:
                    isMatch = False
                    break
                elif currentPatternValue == 0:
                    if valB != valA:
                        isMatch = False
                        break
                else:  # currentPatternValue == -3 (i.e., -6 + 3)
                    if valB >= valA:
                        isMatch = False
                        break
                innerPosition += 1
            if isMatch:
                tally += 1
            outerIndex += 1
        return tally