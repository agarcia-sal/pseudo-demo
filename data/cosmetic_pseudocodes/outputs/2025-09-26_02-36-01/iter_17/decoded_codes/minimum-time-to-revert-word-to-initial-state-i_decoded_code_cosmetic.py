class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        lengthValue = len(word)
        counter = 1
        while True:
            productValue = counter * k
            if productValue >= lengthValue:
                return counter
            substringA = word[productValue:lengthValue]
            substringB = word[0:lengthValue - productValue]
            if substringA == substringB:
                return counter
            counter += 1