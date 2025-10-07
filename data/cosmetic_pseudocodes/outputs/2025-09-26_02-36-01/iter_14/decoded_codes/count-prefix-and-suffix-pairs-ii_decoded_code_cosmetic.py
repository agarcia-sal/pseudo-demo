from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalMatches = 0
        frequencyMap = defaultdict(int)
        index = len(words)
        while index > 0:
            index -= 1
            currentWord = words[index]
            for recordedKey in frequencyMap:
                # Check if currentWord is both prefix and suffix of recordedKey
                if not (currentWord != recordedKey[:len(currentWord)] or 
                        currentWord != recordedKey[-len(currentWord):]):
                    totalMatches += frequencyMap[recordedKey]
            frequencyMap[currentWord] += 1
        return totalMatches