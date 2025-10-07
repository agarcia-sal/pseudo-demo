class Solution:
    def maxSubstringLength(self, s):
        outerPos = 0
        entireFrequency = {}
        maxLen = -1

        while outerPos < len(s):
            innerPos = outerPos
            currentFrequency = {}

            while innerPos < len(s):
                currentChar = s[innerPos]
                if currentChar not in currentFrequency:
                    currentFrequency[currentChar] = 0
                currentFrequency[currentChar] += 1
                innerPos += 1

                if outerPos == 0:
                    entireFrequency.clear()
                    for c in s:
                        entireFrequency[c] = entireFrequency.get(c, 0) + 1

                isValid = True
                charList = list(currentFrequency.keys())
                idx = 0
                while idx < len(charList) and isValid:
                    ch = charList[idx]
                    if currentFrequency[ch] < entireFrequency[ch]:
                        isValid = False
                    idx += 1

                if isValid and len(charList) < len(entireFrequency):
                    windowLength = innerPos - outerPos
                    if maxLen < windowLength:
                        maxLen = windowLength

            outerPos += 1

        return maxLen