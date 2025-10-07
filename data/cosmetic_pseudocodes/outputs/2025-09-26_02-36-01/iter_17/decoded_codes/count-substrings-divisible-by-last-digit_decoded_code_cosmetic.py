class Solution:
    def countSubstrings(self, s: str) -> int:
        lengthOfStr = 0
        while lengthOfStr < len(s):
            lengthOfStr += 1

        aggregateCount = 0
        outerIndex = 0

        while True:
            if outerIndex >= lengthOfStr:
                break

            numericAccumulator = 0
            innerIndex = outerIndex

            while innerIndex < lengthOfStr:
                digitChar = s[innerIndex]
                digitVal = int(digitChar)
                numericAccumulator = (numericAccumulator * 10) + digitVal

                if digitVal != 0:
                    if numericAccumulator % digitVal == 0:
                        aggregateCount += 1

                innerIndex += 1

            outerIndex += 1

        return aggregateCount