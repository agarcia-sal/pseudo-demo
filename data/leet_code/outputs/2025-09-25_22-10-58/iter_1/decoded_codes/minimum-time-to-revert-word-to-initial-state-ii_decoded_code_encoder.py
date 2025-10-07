class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        time = 1
        while True:
            prefix_to_match = word[time * k:]
            if word.startswith(prefix_to_match):
                return time
            time += 1