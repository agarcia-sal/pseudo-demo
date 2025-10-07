class Solution:
    def countSubstrings(self, s: str) -> int:
        resultCount = 0
        lengthVar = len(s)
        startIndex = 0
        while startIndex <= lengthVar - 1:
            accumulator = 0
            endIndex = startIndex
            while endIndex <= lengthVar - 1:
                digitValue = int(s[endIndex])
                accumulator = accumulator * 10 + digitValue
                if digitValue != 0 and (accumulator % digitValue) == 0:
                    resultCount += 1
                endIndex += 1
            startIndex += 1
        return resultCount