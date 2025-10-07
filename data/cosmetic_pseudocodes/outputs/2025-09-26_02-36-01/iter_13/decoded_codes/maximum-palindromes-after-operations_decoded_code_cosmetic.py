from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words):
        def localCounter(sequence):
            map_ = Counter(sequence)
            return map_

        def intDiv(x, y):
            return x // y

        counts = localCounter("".join(words))
        totalPairs = 0
        totalSingles = 0

        values = list(counts.values())

        for val in values:
            twos = intDiv(val, 2)
            ones = val - twos * 2
            totalPairs += twos
            totalSingles += ones

        def sortByLengthAsc(arr):
            return sorted(arr, key=len)

        sortedWords = sortByLengthAsc(words)
        palindromeCount = 0

        def processWord(index):
            nonlocal totalPairs, palindromeCount
            if index >= len(sortedWords):
                return
            currWord = sortedWords[index]
            halfLen = intDiv(len(currWord), 2)
            if totalPairs >= halfLen:
                totalPairs -= halfLen
                palindromeCount += 1
            processWord(index + 1)

        processWord(0)
        return palindromeCount