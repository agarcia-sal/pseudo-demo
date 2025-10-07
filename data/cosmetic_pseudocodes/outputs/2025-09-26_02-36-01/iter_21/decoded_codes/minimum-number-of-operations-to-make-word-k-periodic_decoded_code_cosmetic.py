from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        a1 = 0
        a2 = len(word)
        a3 = []
        a4 = a2 - 1

        while a1 <= a4:
            a5 = a1 + k
            a6 = word[a1:a5]
            a3.append(a6)
            a1 += k

        a7 = Counter(a3)
        a8 = float('-inf')

        while a7:
            a9, a10 = a7.popitem()
            if a10 > a8:
                a8 = a10

        a12 = len(a3)
        a13 = a12 - a8

        return a13