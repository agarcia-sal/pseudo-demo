class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        length = len(word)
        counter = 1
        while True:
            index = counter * k
            if index >= length or word[index:] == word[:length - index]:
                return counter
            counter += 1