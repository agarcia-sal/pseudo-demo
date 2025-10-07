class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowelSet = {"a", "e", "i", "o", "u"}
        oddSegmentCount = 0
        vowelCount = 0

        for char in s:
            if char in vowelSet:
                vowelCount += 1

        toggleSegment = False

        for char in s:
            if char in vowelSet:
                toggleSegment = not toggleSegment

            if toggleSegment:
                vowelCount += 1
            elif not toggleSegment and vowelCount % 2 == 1:
                oddSegmentCount += 1
                vowelCount = 0

        if toggleSegment and vowelCount % 2 == 1:
            oddSegmentCount += 1

        return (oddSegmentCount % 2) == 1