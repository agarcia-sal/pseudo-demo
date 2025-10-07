class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelSet = {"a", "e", "i", "o", "u"}
        countOddSegments = 0
        vowelCounter = 0

        index = 0
        while index < len(s):
            char = s[index]
            if char in vowelSet:
                vowelCounter += 1
            index += 1

        isOddSegmentActive = False
        pos = 0
        while pos < len(s):
            letter = s[pos]
            if letter in vowelSet:
                isOddSegmentActive = not isOddSegmentActive

            if isOddSegmentActive:
                vowelCounter += 1
            else:
                if vowelCounter % 2 != 0:
                    countOddSegments += 1
                    vowelCounter = 0
            pos += 1

        if isOddSegmentActive and (vowelCounter % 2 != 0):
            countOddSegments += 1

        return (countOddSegments % 2) == 1