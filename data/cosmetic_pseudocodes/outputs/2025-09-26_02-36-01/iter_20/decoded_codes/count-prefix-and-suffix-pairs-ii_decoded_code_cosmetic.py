from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        def equalsSubstring(source, startIndex, endIndex, sub):
            length_sub = len(sub)
            # Check if the segment length matches sub length
            if (endIndex - startIndex + 1) != length_sub:
                return False
            for i in range(length_sub):
                if source[startIndex + i] != sub[i]:
                    return False
            return True

        totalPairs = 0
        lookupMap = defaultdict(int)

        for idxOuter in range(len(words) - 1, -1, -1):
            currentWord = words[idxOuter]
            for candidateKey in lookupMap.keys():
                if equalsSubstring(candidateKey, 0, len(currentWord) - 1, currentWord) and \
                   equalsSubstring(candidateKey, len(candidateKey) - len(currentWord), len(candidateKey) - 1, currentWord):
                    totalPairs += lookupMap[candidateKey]
            lookupMap[currentWord] += 1

        return totalPairs