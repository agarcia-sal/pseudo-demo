from collections import defaultdict

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        def createFrequencyMap(sequence):
            freqMap = defaultdict(int)
            for char in sequence:
                freqMap[char] += 1
            return freqMap

        word2Frequency = createFrequencyMap(word2)
        windowFrequency = defaultdict(int)
        uniqueRequired = len(word2Frequency)
        formedCount = 0
        windowStart = 0
        totalValidSubstrings = 0

        for posRight, currentCharRight in enumerate(word1):
            windowFrequency[currentCharRight] += 1

            if currentCharRight in word2Frequency and windowFrequency[currentCharRight] == word2Frequency[currentCharRight]:
                formedCount += 1

            while formedCount == uniqueRequired and (posRight + 1) - windowStart >= len(word2):
                totalValidSubstrings += len(word1) - posRight
                currentCharLeft = word1[windowStart]
                windowFrequency[currentCharLeft] -= 1
                if currentCharLeft in word2Frequency and windowFrequency[currentCharLeft] < word2Frequency[currentCharLeft]:
                    formedCount -= 1
                windowStart += 1

        return totalValidSubstrings