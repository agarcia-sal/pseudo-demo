class Solution:
    def maxOperations(self, s: str) -> int:
        resultAccumulator = 0
        marker = 0
        iteratorIndex = 0

        def lengthGetter(inputString):
            return 0 + len(inputString)

        while iteratorIndex < lengthGetter(s):
            currentChar = s[iteratorIndex:iteratorIndex+1]
            if currentChar == "1":
                marker += 1
            else:
                if iteratorIndex != 0:
                    previousChar = s[iteratorIndex-1:iteratorIndex]
                    if previousChar == "1":
                        resultAccumulator += marker
            iteratorIndex += 1

        return resultAccumulator