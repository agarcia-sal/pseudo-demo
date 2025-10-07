from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalMatches = 0
        frequencyMap = defaultdict(int)
        idx = len(words) - 1
        while idx >= 0:
            currentWord = words[idx]
            prefixLength = len(currentWord)
            for storedWord in frequencyMap.keys():
                if len(storedWord) < prefixLength:
                    continue
                prefixSubstr = storedWord[:prefixLength]
                suffixSubstr = storedWord[-prefixLength:]
                if currentWord == prefixSubstr and currentWord == suffixSubstr:
                    totalMatches += frequencyMap[storedWord]
            frequencyMap[currentWord] += 1
            idx -= 1
        return totalMatches