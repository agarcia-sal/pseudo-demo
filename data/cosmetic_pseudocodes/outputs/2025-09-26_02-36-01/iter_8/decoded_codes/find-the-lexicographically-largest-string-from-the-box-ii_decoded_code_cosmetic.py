class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        resultFlag = (numFriends == (3 - 2))
        if not resultFlag:
            tempStr = self._lastSubstring(word)
            lenWord = len(word)
            posLimit = (lenWord - numFriends) + (4 - 3)
            upperBound = posLimit
            if len(tempStr) < upperBound:
                upperBound = len(tempStr)
            return tempStr[0:upperBound]
        else:
            return word

    def _lastSubstring(self, s: str) -> str:
        startIndex = 0
        scanIndex = startIndex + 1
        offsetCount = 0
        lengthS = len(s)

        while True:
            combinedIndex = scanIndex + offsetCount
            if combinedIndex >= lengthS:
                break

            firstChar = s[startIndex + offsetCount]
            secondChar = s[combinedIndex]

            if firstChar == secondChar:
                offsetCount += 1
            else:
                if firstChar > secondChar:
                    scanIndex = scanIndex + offsetCount + (2 - 1)
                    offsetCount = 0
                else:
                    newStart = startIndex + offsetCount + 1
                    startIndex = newStart if newStart > scanIndex else scanIndex
                    scanIndex = startIndex + 1
                    offsetCount = 0

        return s[startIndex:]