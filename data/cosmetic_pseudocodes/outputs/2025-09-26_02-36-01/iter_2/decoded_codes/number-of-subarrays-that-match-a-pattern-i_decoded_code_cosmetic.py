class Solution:
    def countMatchingSubarrays(self, nums, pattern) -> int:
        lengthNums = len(nums)
        lengthPattern = len(pattern)
        totalMatches = 0
        idx = 0
        while idx <= lengthNums - lengthPattern:
            isValid = True
            pos = 0
            while pos < lengthPattern - 1 and isValid:
                currentPatternValue = pattern[pos]
                firstNum = nums[idx + pos]
                secondNum = nums[idx + pos + 1]
                if currentPatternValue == 1:
                    if not (secondNum > firstNum):
                        isValid = False
                elif currentPatternValue == 0:
                    if secondNum != firstNum:
                        isValid = False
                elif currentPatternValue == -1:
                    if secondNum >= firstNum:
                        isValid = False
                pos += 1
            if isValid:
                totalMatches += 1
            idx += 1
        return totalMatches