class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        candidateSubstring = self._lastSubstring(word)
        allowedLength = len(word) - numFriends + 1
        resultLength = min(len(candidateSubstring), allowedLength)
        return candidateSubstring[:resultLength]

    def _lastSubstring(self, s: str) -> str:
        startIndex, compareIndex, offset = 0, 1, 0
        length = len(s)

        while compareIndex + offset < length:
            charAtStart = s[startIndex + offset]
            charAtCompare = s[compareIndex + offset]

            if charAtStart == charAtCompare:
                offset += 1
            elif charAtStart > charAtCompare:
                compareIndex += offset + 1
                offset = 0
            else:
                startIndex = max(startIndex + offset + 1, compareIndex)
                compareIndex = startIndex + 1
                offset = 0

        return s[startIndex:]