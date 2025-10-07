class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        fz = len(word)
        sq = 1
        while True:
            if (sq * k >= fz) or (word[sq * k:] == word[:fz - sq * k]):
                return sq
            sq += 1