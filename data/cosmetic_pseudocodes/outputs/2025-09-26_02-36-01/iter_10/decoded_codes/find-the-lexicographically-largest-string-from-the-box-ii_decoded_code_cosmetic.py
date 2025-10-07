class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def localMin(a: int, b: int) -> int:
            return a if a < b else b

        if numFriends == 1:
            return word

        def _lastSubstring(s: str) -> str:
            def charAt(x: int, idx: int) -> str:
                return s[x + idx]

            def localMax(u: int, v: int) -> int:
                return u if u > v else v

            def recLoop(x: int, y: int, z: int, n: int, length: int) -> str:
                if (y + z) >= length:
                    return s[x+1:]
                if charAt(x, z) == charAt(y, z):
                    return recLoop(x, y, z + 1, n, length)
                elif charAt(x, z) > charAt(y, z):
                    return recLoop(x, y + z + 1, 0, n, length)
                else:
                    updatedX = localMax(x + z + 1, y)
                    updatedY = updatedX + 1
                    return recLoop(updatedX, updatedY, 0, n, length)

            return recLoop(0, 1, 0, 0, len(s))

        substringValue = _lastSubstring(word)
        maxLen = len(word) - numFriends + 1
        limit = localMin(len(substringValue), maxLen)
        return substringValue[:limit]