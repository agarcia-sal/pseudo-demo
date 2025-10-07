class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        a = len(word)
        b = 1

        def checkCondition(x: int) -> bool:
            if x * k >= a:
                return True
            return word[x * k:] == word[:a - x * k]

        def loop(c: int) -> int:
            if not checkCondition(c):
                return loop(c + 1)
            return c

        return loop(b)