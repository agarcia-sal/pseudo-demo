class Solution:
    def minOperations(self, chars):
        opCount = 0
        toggleState = 0
        idx = 1
        lengthVal = 0

        while True:
            if not (idx <= len(chars)):
                break
            element = chars[idx - 1]  # convert 1-based to 0-based indexing
            if (toggleState % 2) == 0:
                transformed = element
            else:
                transformed = 1 - element
            if not (transformed != 0):
                opCount += 1
                toggleState += 1
            idx += 1

        return opCount