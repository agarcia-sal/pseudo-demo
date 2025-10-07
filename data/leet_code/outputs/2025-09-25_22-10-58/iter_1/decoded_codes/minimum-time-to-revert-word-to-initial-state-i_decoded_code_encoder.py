class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        time = 1
        while True:
            if time * k >= n or word[time * k :] == word[: n - time * k]:
                return time
            time += 1