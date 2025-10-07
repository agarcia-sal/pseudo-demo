class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        current_time = 1
        while True:
            start = current_time * k
            if start >= length:
                break
            segment = word[start:]
            if word.startswith(segment):
                return current_time
            current_time += 1
        # If no such time found, though problem implies always found, return -1 as fallback
        return -1