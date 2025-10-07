class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        totalLength = len(nums)
        patternLength = len(pattern)
        resultCounter = 0

        def checkPatternAllowed(startIndex, patternIndex, isValid):
            if patternIndex >= patternLength - 1:
                return isValid
            currentPatternVal = pattern[patternIndex]
            firstElement = nums[startIndex + patternIndex]
            secondElement = nums[startIndex + patternIndex + 1]
            if currentPatternVal == 1:
                if not (secondElement > firstElement):
                    return False
            elif currentPatternVal == 0:
                if secondElement != firstElement:
                    return False
            elif currentPatternVal == -1:
                if not (secondElement < firstElement):
                    return False
            return checkPatternAllowed(startIndex, patternIndex + 1, isValid)

        iterationIndex = 0
        while iterationIndex <= totalLength - patternLength:
            if checkPatternAllowed(iterationIndex, 0, True):
                resultCounter += 1
            iterationIndex += 1

        return resultCounter