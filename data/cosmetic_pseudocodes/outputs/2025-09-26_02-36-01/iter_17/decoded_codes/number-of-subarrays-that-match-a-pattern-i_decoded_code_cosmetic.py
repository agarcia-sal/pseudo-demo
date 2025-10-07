class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        totalElements = len(nums)
        patternLength = len(pattern)
        resultCounter = 0

        currentIndex = 0
        while currentIndex <= totalElements - patternLength - 1:
            isValidSubarray = True
            innerIndex = 0

            while innerIndex < patternLength - 1:
                patternValue = pattern[innerIndex]
                firstVal = nums[currentIndex + innerIndex]
                secondVal = nums[currentIndex + innerIndex + 1]

                if patternValue == 1 and secondVal > firstVal:
                    innerIndex += 1
                elif patternValue == 0 and secondVal == firstVal:
                    innerIndex += 1
                elif patternValue == -1 and secondVal < firstVal:
                    innerIndex += 1
                else:
                    isValidSubarray = False
                    break

            if isValidSubarray:
                resultCounter += 1

            currentIndex += 1

        return resultCounter