class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length_of_word = len(word)
        elapsed = 1
        while True:
            segment = word[elapsed * k :]
            starts_match = word.startswith(segment)
            if starts_match:
                return elapsed
            elapsed += 1