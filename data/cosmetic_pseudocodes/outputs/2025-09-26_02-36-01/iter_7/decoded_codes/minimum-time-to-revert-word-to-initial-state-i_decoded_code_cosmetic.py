class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        m = len(word)
        c = 1
        while True:
            x = c * k
            if x >= m or word[x:m] == word[0:m - x]:
                return c
            c += 1