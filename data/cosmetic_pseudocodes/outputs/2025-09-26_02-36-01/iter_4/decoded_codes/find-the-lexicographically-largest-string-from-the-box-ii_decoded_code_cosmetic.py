class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        lastSubstr = self._lastSubstring(word)
        limit = len(word) - numFriends + 1
        endPos = len(lastSubstr) if len(lastSubstr) < limit else limit
        return lastSubstr[:endPos]

    def _lastSubstring(self, s: str) -> str:
        idxA, idxB, offset = 0, 1, 0
        n = len(s)
        while idxB + offset < n:
            if s[idxA + offset] == s[idxB + offset]:
                offset += 1
            else:
                if s[idxA + offset] > s[idxB + offset]:
                    idxB = idxB + offset + 1
                    offset = 0
                else:
                    newIdxA = idxA + offset + 1
                    idxA = newIdxA if newIdxA > idxB else idxB
                    idxB = idxA + 1
                    offset = 0
        return s[idxA:]