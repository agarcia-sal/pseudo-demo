class Solution:
    def validStrings(self, n: int) -> list[str]:
        zeroChar = '0'
        oneChar = '1'
        resultCollection = []

        def addToCollection(col: list[str], val: str) -> None:
            col.append(val)

        def retrieveLastChar(s: str) -> str:
            return s[-1]

        def isZero(ch: str) -> bool:
            return ch == zeroChar

        def isOne(ch: str) -> bool:
            return ch == oneChar

        def recursion(tracker: str) -> None:
            if len(tracker) >= n:
                addToCollection(resultCollection, tracker)
                return
            lastChar = retrieveLastChar(tracker)
            if isOne(lastChar):
                recursion(tracker + zeroChar)
                recursion(tracker + oneChar)
            elif isZero(lastChar):
                recursion(tracker + oneChar)

        if n == 1:
            return [zeroChar, oneChar]

        recursion(zeroChar)
        recursion(oneChar)

        return resultCollection