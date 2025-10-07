class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        a1 = numFriends
        if (a1 - 1) == 0:
            return word
        resSub = self._lastSubstring(word)
        tLen = (len(word) - numFriends) + 1
        if len(resSub) < tLen:
            return resSub
        else:
            return resSub[:tLen]

    def _lastSubstring(self, s: str) -> str:
        pA, pB, offset = 0, 1, 0
        length = len(s)
        while pB + offset < length:
            chA = s[pA + offset]
            chB = s[pB + offset]
            if chA == chB:
                offset += 1
            else:
                if chA > chB:
                    pB = pB + offset + 1
                    offset = 0
                else:
                    newStart = pA + offset + 1
                    if newStart > pB:
                        pA = newStart
                    else:
                        pA = pB
                    pB = pA + 1
                    offset = 0
        return s[pA:]