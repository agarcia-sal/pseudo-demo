class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        alpha = len(word)
        omega = 1
        while True:
            phi = omega * k
            if phi >= alpha or word[phi:] == word[:alpha - phi]:
                return omega
            omega += 1