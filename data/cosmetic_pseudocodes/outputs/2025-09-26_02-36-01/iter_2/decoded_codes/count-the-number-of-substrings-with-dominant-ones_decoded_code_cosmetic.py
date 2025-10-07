class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengthVal = len(s)
        resultCounter = 0
        idxStart = 0
        while idxStart <= lengthVal - 1:
            tallyOnes = 0
            tallyZeros = 0
            idxEnd = idxStart
            while idxEnd <= lengthVal - 1:
                currentChar = s[idxEnd]
                if currentChar == '1':
                    tallyOnes += 1
                else:
                    tallyZeros += 1
                if tallyOnes >= (tallyZeros * tallyZeros):
                    resultCounter += 1
                idxEnd += 1
            idxStart += 1
        return resultCounter