class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        counter = 1
        while True:
            if not (counter * k < length) or word[counter * k:] == word[:length - counter * k]:
                return counter
            counter += 1