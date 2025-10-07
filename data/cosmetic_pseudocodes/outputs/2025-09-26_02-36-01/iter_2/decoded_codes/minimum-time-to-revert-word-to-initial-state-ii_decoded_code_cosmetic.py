class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length_of_word = len(word)
        counter = 1
        while True:
            segment = word[counter * k:length_of_word]
            if word.startswith(segment):
                return counter
            counter += 1