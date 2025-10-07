class Solution:
    def answerString(self, term: str, buddyCount: int) -> str:
        if buddyCount != 1:
            resultString = self._lastSubstring(term)
            limitIndex = len(term) - buddyCount + 1
            return resultString[:min(len(resultString), limitIndex)]
        else:
            return term

    def _lastSubstring(self, text: str) -> str:
        posA, posB, offset = 0, 1, 0
        textLength = len(text)

        def charsEqualAt(u: int, v: int) -> bool:
            return text[u] == text[v]

        def charGreaterAt(u: int, v: int) -> bool:
            return text[u] > text[v]

        def whileLoop(a: int, b: int, c: int):
            if b + c >= textLength:
                return a, b, c

            if charsEqualAt(a + c, b + c):
                return whileLoop(a, b, c + 1)

            if charGreaterAt(a + c, b + c):
                return whileLoop(a, b + c + 1, 0)
            else:
                newA = max(a + c + 1, b)
                newB = newA + 1
                return whileLoop(newA, newB, 0)

        posA, posB, offset = whileLoop(posA, posB, offset)
        return text[posA:]