class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        countFriends = numFriends
        inputWord = word
        if countFriends == 1:
            return inputWord
        lastSub = self._lastSubstring(inputWord)
        limit = (len(inputWord) - countFriends) + 1
        endIndex = len(lastSub) if len(lastSub) < limit else limit
        return lastSub[:endIndex]

    def _lastSubstring(self, s: str) -> str:
        firstIndex = 0
        secondIndex = 1
        offset = 0
        strLength = len(s)

        while True:
            if (secondIndex + offset) >= strLength:
                break

            charAtFirst = s[firstIndex + offset]
            charAtSecond = s[secondIndex + offset]

            if charAtFirst == charAtSecond:
                offset += 1
                continue

            if charAtFirst > charAtSecond:
                secondIndex = secondIndex + offset + 1
                offset = 0
                continue

            firstIndex = max(firstIndex + offset + 1, secondIndex)
            secondIndex = firstIndex + 1
            offset = 0

        return s[firstIndex:]