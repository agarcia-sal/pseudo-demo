class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        alpha = 1
        beta = len(word)
        while True:
            if not (alpha * k < beta) or (word[alpha * k:beta] == word[0:(beta - alpha * k)]):
                return alpha
            alpha += 1