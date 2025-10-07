class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        xU34 = self._lastSubstring(word)
        w7V2 = len(word) - numFriends + 1
        z90K = len(xU34)
        if w7V2 < z90K:
            z90K = w7V2
        return xU34[:z90K]

    def _lastSubstring(self, s: str) -> str:
        a, b, c = 0, 1, 0
        n = len(s)
        while True:
            if b + c >= n:
                break
            p1 = s[a + c]
            p2 = s[b + c]
            if p1 == p2:
                c += 1
            else:
                if p1 > p2:
                    b = b + c + 1
                    c = 0
                else:
                    a = max(a + c + 1, b)
                    b = a + 1
                    c = 0
            if b >= n:
                break
        return s[a:]