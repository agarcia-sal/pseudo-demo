class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        alpha = len(word)
        omega = 1
        while True:
            beta = word[omega * k : alpha]
            if word.startswith(beta):
                return omega
            omega += 1