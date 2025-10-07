from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        letterFrequency = Counter()
        for text in words:
            letterFrequency.update(text)

        numberOfPairs = 0
        numberOfSingles = 0
        freqValues = list(letterFrequency.values())
        idx = 0
        while idx < len(freqValues):
            freqValue = freqValues[idx]
            pairsCount = freqValue // 2
            singleCount = freqValue - pairsCount * 2
            numberOfPairs += pairsCount
            numberOfSingles += singleCount
            idx += 1

        orderedWords = sorted(words, key=len)
        palindromeCount = 0
        for currentWord in orderedWords:
            midPoint = len(currentWord) // 2
            if numberOfPairs >= midPoint:
                numberOfPairs -= midPoint
                palindromeCount += 1

        return palindromeCount