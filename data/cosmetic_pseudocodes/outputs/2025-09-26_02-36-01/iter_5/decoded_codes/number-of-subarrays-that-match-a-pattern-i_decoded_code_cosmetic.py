class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        lenNums = len(nums)
        lenPattern = len(pattern)
        totalMatches = 0

        def verifyMatch(startIndex, offset):
            if offset == lenPattern:
                return 1
            symbol = pattern[offset]
            currentVal = nums[startIndex + offset]
            nextVal = nums[startIndex + offset + 1]

            if symbol == 1:
                isMatch = not (nextVal <= currentVal)
            elif symbol == 0:
                isMatch = (nextVal == currentVal)
            elif symbol == -1:
                isMatch = not (nextVal >= currentVal)
            else:
                isMatch = False

            if isMatch:
                return verifyMatch(startIndex, offset + 1)
            else:
                return 0

        currentIndex = 0
        while currentIndex < lenNums - lenPattern:
            totalMatches += verifyMatch(currentIndex, 0)
            currentIndex += 1

        return totalMatches