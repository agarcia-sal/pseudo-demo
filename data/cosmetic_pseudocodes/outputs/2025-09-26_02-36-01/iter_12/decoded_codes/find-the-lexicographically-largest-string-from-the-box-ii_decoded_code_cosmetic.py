class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        def minVal(x: int, y: int) -> int:
            return x if x < y else y

        def lengthOf(s: str) -> int:
            return len(s)

        if numFriends == 1:
            return word

        freshStr = self._lastSubstring(word)
        limitVal = lengthOf(word) - numFriends + 1

        # substring(s, start, end) with 1-based start index, end exclusive
        # so substring freshStr[0:limit] with limit=minVal(lengthOf(freshStr), limitVal)
        return freshStr[:minVal(lengthOf(freshStr), limitVal)]

    def _lastSubstring(self, s: str) -> str:
        lengthVal = len(s)

        def charAt(str_: str, idx: int) -> str:
            return str_[idx]

        def maxVal(a: int, b: int) -> int:
            return a if a > b else b

        def loopCondition(i: int, j: int, k: int, lengthVal: int) -> bool:
            return (j + k) < lengthVal

        newI = 0
        iteratorJ = 1
        offsetK = 0

        while True:
            if not loopCondition(newI, iteratorJ, offsetK, lengthVal):
                break

            firstChar = charAt(s, newI + offsetK)
            secondChar = charAt(s, iteratorJ + offsetK)

            if firstChar == secondChar:
                offsetK += 1
            else:
                if firstChar > secondChar:
                    iteratorJ = iteratorJ + offsetK + 1
                    offsetK = 0
                else:
                    newI = maxVal(newI + offsetK + 1, iteratorJ)
                    iteratorJ = newI + 1
                    offsetK = 0

        # substring(s, start, end) with 1-based start
        # so substring(s, newI+1, lengthVal) means s[newI:] in python 0-based
        return s[newI:]