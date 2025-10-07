class Solution:
    def minAnagramLength(self, s: str) -> int:
        distinctSymbols = set()
        indexCounter = 0
        while indexCounter < len(s):
            currentElement = s[indexCounter]
            distinctSymbols.add(currentElement)
            indexCounter += 1
        resultValue = len(distinctSymbols)
        return resultValue