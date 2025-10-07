from collections import defaultdict

class Solution:
    def maxPalindromesAfterOperations(self, words):
        ZERO_VALUE = 0
        charFrequency = defaultdict(lambda: ZERO_VALUE)
        totalPairs = ZERO_VALUE
        totalSingles = ZERO_VALUE
        resultPalindromes = ZERO_VALUE

        def accumulateChars(listOfWords):
            iter_ = 0
            while True:
                if iter_ >= len(listOfWords):
                    return
                currentWord = listOfWords[iter_]
                charIndex = 0
                while charIndex < len(currentWord):
                    currentChar = currentWord[charIndex]
                    # Increment the frequency of the current character
                    charFrequency[currentChar] = charFrequency[currentChar] + 1
                    charIndex += 1
                iter_ += 1

        accumulateChars(words)

        freqValues = [charFrequency[key] for key in charFrequency]

        def processCounts(counts):
            nonlocal totalPairs, totalSingles
            index = 0
            while index < len(counts):
                singleCount = counts[index]
                totalPairs += singleCount // 2
                totalSingles += singleCount % 2
                index += 1

        processCounts(freqValues)

        # Sort words by length in ascending order
        sortedWords = sorted(words, key=len)

        wordIdx = 0
        while True:
            if wordIdx >= len(sortedWords):
                break
            curWord = sortedWords[wordIdx]
            halfLen = len(curWord) // 2
            if totalPairs >= halfLen:
                totalPairs -= halfLen
                resultPalindromes += 1
            wordIdx += 1

        return resultPalindromes