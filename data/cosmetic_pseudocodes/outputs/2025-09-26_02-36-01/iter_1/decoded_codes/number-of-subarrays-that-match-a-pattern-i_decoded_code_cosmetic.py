class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        totalLength = len(nums)
        patternLength = len(pattern)
        resultCount = 0
        for startIndex in range(totalLength - patternLength):
            isValid = True
            for offset in range(patternLength - 1):
                currentPatternValue = pattern[offset]
                currentNum = nums[startIndex + offset]
                nextNum = nums[startIndex + offset + 1]
                if currentPatternValue == 1:
                    if nextNum <= currentNum:
                        isValid = False
                        break
                elif currentPatternValue == 0:
                    if nextNum != currentNum:
                        isValid = False
                        break
                elif currentPatternValue == -1:
                    if nextNum >= currentNum:
                        isValid = False
                        break
            if isValid:
                resultCount += 1
        return resultCount