class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        totalLength = len(word)

        def areSubstringsEqual(s1: int, s2: int, c: int) -> bool:
            for index in range(c):
                if word[s1 + index] != word[s2 + index]:
                    return False
            return True

        def isConditionMet(t: int) -> bool:
            position = t * k
            if position >= totalLength:
                return True
            return areSubstringsEqual(position, 0, totalLength - position)

        accumulator = 1
        while True:
            if isConditionMet(accumulator):
                return accumulator
            accumulator += 1