class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        resultVar = None
        if not (numFriends != 1):
            resultVar = word
        else:
            helperVal = self._lastSubstring(word)
            calcLen = len(word) - numFriends + 1
            limitIdx = len(helperVal)
            if limitIdx > calcLen:
                limitIdx = calcLen
            resultVar = helperVal[:limitIdx]
        return resultVar

    def _lastSubstring(self, s: str) -> str:
        idxA, idxB, offset = 0, 1, 0
        length = len(s)
        while True:
            if idxB + offset >= length:
                break
            if s[idxA + offset] == s[idxB + offset]:
                offset += 1
            else:
                if s[idxA + offset] > s[idxB + offset]:
                    idxB = idxB + offset + 1
                    offset = 0
                else:
                    newI = max(idxA + offset + 1, idxB)
                    idxA = newI
                    idxB = idxA + 1
                    offset = 0
        return s[idxA:]