from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalMatches = 0
        frequencyMap = defaultdict(int)
        index = len(words) - 1
        while index >= 0:
            currentWord = words[index]
            for entryKey in list(frequencyMap.keys()):
                prefixValid = (currentWord == entryKey[:len(currentWord)])
                suffixValid = (currentWord == entryKey[-len(currentWord):])
                if prefixValid and suffixValid:
                    totalMatches += frequencyMap[entryKey]
            frequencyMap[currentWord] += 1
            index -= 1
        return totalMatches