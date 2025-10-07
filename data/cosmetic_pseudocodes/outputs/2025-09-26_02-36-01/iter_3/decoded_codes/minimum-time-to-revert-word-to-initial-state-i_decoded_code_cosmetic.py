class Solution:
    def minimumTimeToInitialState(self, k: int, word: str) -> int:
        lengthVar = len(word)
        counter = 1
        while True:
            product = counter * k
            if product >= lengthVar:
                return counter
            suffixSubstr = word[product:lengthVar]
            prefixSubstr = word[0:lengthVar - product]
            if suffixSubstr == prefixSubstr:
                return counter
            counter += 1