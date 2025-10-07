class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        a = len(word)
        b = 1
        while True:
            if not (b * k < a) or word[b * k:a] == word[:a - b * k]:
                return b
            b += 1