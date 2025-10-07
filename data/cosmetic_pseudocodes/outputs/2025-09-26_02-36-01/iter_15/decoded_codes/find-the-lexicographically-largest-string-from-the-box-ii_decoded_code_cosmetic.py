class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends - 1 == 0:
            return word
        alpha = self._lastSubstring(word)
        beta = (len(word) - numFriends) + 1
        return alpha[:min(len(alpha), beta)]

    def _lastSubstring(self, s: str) -> str:
        def proc(u: int, v: int, w: int) -> int:
            if v + w >= len(s):
                return u
            if s[u + w] == s[v + w]:
                return proc(u, v, w + 1)
            if s[u + w] > s[v + w]:
                return proc(u, v + w + 1, 0)
            m = u + w + 1 if u + w + 1 > v else v
            return proc(m, m + 1, 0)

        idx = proc(0, 1, 0)
        startPos = idx + 1
        endPos = len(s)
        # slicing string from startPos (1-based index) to end (exclusive in Python)
        # So adjust for 1-based indexing in pseudocode to 0-based in Python
        return s[startPos:endPos]