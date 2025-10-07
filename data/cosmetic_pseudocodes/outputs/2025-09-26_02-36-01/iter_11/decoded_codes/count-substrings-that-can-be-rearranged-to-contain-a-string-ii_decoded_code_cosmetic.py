from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        alpha = Counter(word2)
        beta = Counter()
        quota = len(alpha)
        tally = 0
        front = 0
        outcome = 0

        def incrementCount(key, dictionary):
            dictionary[key] = dictionary.get(key, 0) + 1

        def decrementCount(key, dictionary):
            dictionary[key] = dictionary.get(key, 0) - 1

        def meetsRequired(key):
            return key in alpha and beta.get(key, 0) == alpha[key]

        def lacksRequired(key):
            return key in alpha and beta.get(key, 0) < alpha[key]

        def recurProcess(tail, start, acc, formedCount):
            if tail < len(word1):
                incrementCount(word1[tail], beta)

                if meetsRequired(word1[tail]):
                    formedCount += 1

                while formedCount == quota and tail + 1 - start >= len(word2):
                    acc += len(word1) - tail
                    decrementCount(word1[start], beta)
                    if lacksRequired(word1[start]):
                        formedCount -= 1
                    start += 1

                return recurProcess(tail + 1, start, acc, formedCount)
            else:
                return acc

        return recurProcess(0, front, outcome, tally)