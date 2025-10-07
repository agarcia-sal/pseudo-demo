class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        x = self._lastSubstring(word)
        m = (len(word) - numFriends) + 1
        t = len(x)
        if m < t:
            t = m
        return x[:t]

    def _lastSubstring(self, s: str) -> str:
        a, b, c = 0, 1, 0
        length = len(s)
        while True:
            if b + c >= length:
                break
            if s[a + c] == s[b + c]:
                c += 1
            else:
                if s[a + c] > s[b + c]:
                    b = b + c + 1
                    c = 0
                else:
                    a = max(a + c + 1, b)
                    b = a + 1
                    c = 0
        return s[a:]