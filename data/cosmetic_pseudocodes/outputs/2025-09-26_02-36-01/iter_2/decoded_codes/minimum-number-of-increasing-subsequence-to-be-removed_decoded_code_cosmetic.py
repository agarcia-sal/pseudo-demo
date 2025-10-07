class Solution:
    def minOperations(self, nums):
        length = len(nums)
        if length == 0:
            return 0
        sequenceLengths = [1] * length
        currentIndex = 1
        while currentIndex < length:
            previousIndex = 0
            while previousIndex < currentIndex:
                if nums[currentIndex] <= nums[previousIndex]:
                    candidateLength = sequenceLengths[previousIndex] + 1
                    if candidateLength > sequenceLengths[currentIndex]:
                        sequenceLengths[currentIndex] = candidateLength
                previousIndex += 1
            currentIndex += 1
        maxLength = sequenceLengths[0]
        pos = 1
        while pos < length:
            if sequenceLengths[pos] > maxLength:
                maxLength = sequenceLengths[pos]
            pos += 1
        return maxLength