from collections import Counter

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        freqMap = Counter(word2)
        winMap = Counter()
        totalNeeded = len(freqMap)
        matched = 0
        startIdx = 0
        resultCount = 0
        pos = 0

        while pos < len(word1):
            currentChar = word1[pos]
            winMap[currentChar] += 1

            if currentChar in freqMap and winMap[currentChar] == freqMap[currentChar]:
                matched += 1

            while matched == totalNeeded and (pos + 1 - startIdx) >= len(word2):
                resultCount += len(word1) - pos

                leftChar = word1[startIdx]
                winMap[leftChar] -= 1
                if leftChar in freqMap and winMap[leftChar] < freqMap[leftChar]:
                    matched -= 1

                startIdx += 1

            pos += 1

        return resultCount