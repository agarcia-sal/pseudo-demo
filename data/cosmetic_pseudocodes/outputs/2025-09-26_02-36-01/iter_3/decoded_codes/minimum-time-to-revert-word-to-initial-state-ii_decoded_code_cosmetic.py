class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length_indicator = len(word)
        counter = 1
        while True:
            start = counter * k
            if start >= length_indicator:
                # If start passes length, segment would be empty or invalid; break to avoid infinite loop
                break
            segment = word[start:length_indicator - start]
            if word.find(segment) == 0:
                return counter
            counter += 1
        # If no such counter found, return -1 or some indication; problem does not specify, so return -1
        return -1