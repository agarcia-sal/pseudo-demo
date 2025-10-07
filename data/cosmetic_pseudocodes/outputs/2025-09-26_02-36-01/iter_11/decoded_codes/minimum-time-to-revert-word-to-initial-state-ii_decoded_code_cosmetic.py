class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        x = 1
        while True:
            suffix = word[x * k :]
            if word.startswith(suffix):
                return x
            x += 1