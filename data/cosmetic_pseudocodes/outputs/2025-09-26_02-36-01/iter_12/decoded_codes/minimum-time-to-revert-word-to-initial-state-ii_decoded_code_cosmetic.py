class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        def checkPrefix(mainStr: str, subStr: str) -> bool:
            # Check if subStr is a prefix of mainStr
            if len(subStr) > len(mainStr):
                return False
            for i in range(len(subStr)):
                if mainStr[i] != subStr[i]:
                    return False
            return True

        strLength = len(word)
        counter = 1

        while True:
            startPos = counter * k
            if startPos >= strLength:
                # If startPos exceeds string length, no further prefixes possible
                break
            tempPrefix = word[startPos:]

            if checkPrefix(word, tempPrefix):
                return counter

            counter += 1