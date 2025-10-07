class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        totalElements = len(nums)
        patternLength = len(pattern)
        validSequences = 0
        startIndex = 0
        while startIndex <= totalElements - patternLength:
            isValid = True
            offset = 0
            while offset < patternLength - 1 and isValid:
                currPatternValue = pattern[offset]
                firstNum = nums[startIndex + offset]
                secondNum = nums[startIndex + offset + 1]
                if currPatternValue == 1:
                    if not (secondNum > firstNum):
                        isValid = False
                elif currPatternValue == 0:
                    if secondNum != firstNum:
                        isValid = False
                elif currPatternValue == -1:
                    if not (secondNum < firstNum):
                        isValid = False
                offset += 1
            if isValid:
                validSequences += 1
            startIndex += 1
        return validSequences