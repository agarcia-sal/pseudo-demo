class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        lengthNums = len(nums)
        lengthPattern = len(pattern)
        totalMatches = 0
        indexIter = 0

        # The loop condition adjusted to prevent index out-of-range when accessing nextNum
        while indexIter <= lengthNums - lengthPattern - 1:
            isValidMatch = True
            innerCounter = 0

            while innerCounter < lengthPattern:
                currentPatternElement = pattern[innerCounter]
                currentNum = nums[indexIter + innerCounter]
                nextNum = nums[indexIter + innerCounter + 1]

                if currentPatternElement == 1:
                    if nextNum <= currentNum:
                        isValidMatch = False
                        break
                elif currentPatternElement == 0:
                    if nextNum != currentNum:
                        isValidMatch = False
                        break
                elif currentPatternElement == -1:
                    if nextNum >= currentNum:
                        isValidMatch = False
                        break
                innerCounter += 1

            if isValidMatch:
                totalMatches += 1
            indexIter += 1

        return totalMatches