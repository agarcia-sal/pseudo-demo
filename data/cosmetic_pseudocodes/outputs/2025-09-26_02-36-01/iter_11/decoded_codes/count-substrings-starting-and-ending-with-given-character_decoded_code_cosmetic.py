class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        lengthVal = 0
        while lengthVal < len(s):
            lengthVal += 1

        freqCounter = 0
        idxVar = 0
        while idxVar < len(s):
            if s[(len(s) - 1) - idxVar] == c:
                freqCounter += 1
            idxVar += 1

        outputVal = (freqCounter * (freqCounter + 1)) // 2
        return outputVal