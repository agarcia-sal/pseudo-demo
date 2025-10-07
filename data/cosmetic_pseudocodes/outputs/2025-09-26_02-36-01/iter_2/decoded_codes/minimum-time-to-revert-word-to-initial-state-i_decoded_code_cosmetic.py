class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        lengthVar = len(word)
        counter = 1
        while True:
            product = counter * k
            if product >= lengthVar or word[product:] == word[:lengthVar - product]:
                return counter
            counter += 1