class Solution:
    def minimumTimeToInitialState(self, k: int, word: str) -> int:
        q = len(word)
        w = 1
        while True:
            r = w * k
            if r >= q or word[r:q] == word[0:q - r]:
                return w
            w += 1