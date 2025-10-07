class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def _minValue(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def _length(s: str) -> int:
            cnt = 0
            while True:
                try:
                    _ = s[cnt]
                    cnt += 1
                except IndexError:
                    break
            return cnt

        def _substring(src: str, startPos: int, endPos: int) -> str:
            result = ""
            p = startPos
            while p < endPos:
                result += src[p]
                p += 1
            return result

        if numFriends == 1:
            return word

        def _lastSubstring(n: str) -> str:
            def _charAt(t: str, idx: int) -> str:
                return t[idx]

            x, y, z = 0, 1, 0
            length_n = _length(n)
            while True:
                if y + z >= length_n:
                    break

                c1 = _charAt(n, x + z)
                c2 = _charAt(n, y + z)
                if c1 == c2:
                    z += 1
                else:
                    if c1 > c2:
                        y = y + z + 1
                        z = 0
                    else:
                        def maximumValue(m: int, n_: int) -> int:
                            if m > n_:
                                return m
                            else:
                                return n_

                        x = maximumValue(x + z + 1, y)
                        y = x + 1
                        z = 0
                if y >= length_n:
                    break

            return _substring(n, x, length_n)

        def maximumValue(m: int, n_: int) -> int:
            if m > n_:
                return m
            else:
                return n_

        s = _lastSubstring(word)
        lengthW = _length(word)
        cutLen = lengthW - numFriends + 1
        endIndex = _minValue(_length(s), cutLen)
        return _substring(s, 0, endIndex)