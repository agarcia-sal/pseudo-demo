class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def is_almost_equal(substring: str, pattern: str) -> bool:
            differenceCounter = 0
            for i in range(len(substring)):
                if substring[i] != pattern[i]:
                    differenceCounter += 1
                    if differenceCounter > 1:
                        return False
            return True

        patternLen = len(pattern)
        limitIndex = len(s) - patternLen + 1
        currentIndex = 0
        while currentIndex < limitIndex:
            if is_almost_equal(s[currentIndex:currentIndex + patternLen], pattern):
                return currentIndex
            currentIndex += 1
        return -1