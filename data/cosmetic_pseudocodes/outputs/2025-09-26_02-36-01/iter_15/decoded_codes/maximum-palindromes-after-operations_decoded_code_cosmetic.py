from collections import Counter
from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        def computeCounts(list_of_strings: List[str]) -> Counter:
            accumulatorMap = Counter()
            for currentStr in list_of_strings:
                for ch in currentStr:
                    accumulatorMap[ch] += 1
            return accumulatorMap

        mapZ = computeCounts(words)
        countPairs = 0
        countSingles = 0
        for currCount in mapZ.values():
            countPairs += currCount // 2
            countSingles += currCount % 2

        sortedWords = words[:]
        n = len(sortedWords)
        for i in range(1, n):
            j = i
            while j > 0 and len(sortedWords[j - 1]) > len(sortedWords[j]):
                sortedWords[j], sortedWords[j - 1] = sortedWords[j - 1], sortedWords[j]
                j -= 1

        palindromeCount = 0
        wordIndex = 0
        while wordIndex < n:
            currentWord = sortedWords[wordIndex]
            hl = len(currentWord) // 2
            if countPairs >= hl:
                countPairs -= hl
                palindromeCount += 1
            wordIndex += 1

        return palindromeCount