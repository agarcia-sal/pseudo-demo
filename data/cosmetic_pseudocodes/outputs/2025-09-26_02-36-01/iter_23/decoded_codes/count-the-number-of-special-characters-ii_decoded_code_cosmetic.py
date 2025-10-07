class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        resultVar = 0
        mapOne = {}
        mapTwo = {}

        def recurseIndices(pos, seq):
            if pos >= len(seq):
                return
            currentChar = seq[pos]
            if currentChar not in mapOne:
                mapOne[currentChar] = pos
            mapTwo[currentChar] = pos
            recurseIndices(pos + 1, seq)

        recurseIndices(0, word)

        charsetLeft = [chr(ord('a') + i) for i in range(26)]
        charsetRight = [chr(ord('A') + j) for j in range(26)]

        def loopCount(index):
            nonlocal resultVar
            if index >= len(charsetLeft):
                return
            lowerChar = charsetLeft[index]
            upperChar = charsetRight[index]
            hasLowerInMapTwo = lowerChar in mapTwo
            hasUpperInMapOne = upperChar in mapOne
            if hasLowerInMapTwo and hasUpperInMapOne:
                if mapTwo[lowerChar] < mapOne[upperChar]:
                    resultVar += 1
            loopCount(index + 1)

        loopCount(0)

        return resultVar