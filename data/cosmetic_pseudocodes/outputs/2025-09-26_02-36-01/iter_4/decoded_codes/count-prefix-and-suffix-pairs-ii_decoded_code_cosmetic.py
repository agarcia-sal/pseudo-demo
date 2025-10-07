from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        frequencyMap = defaultdict(int)
        index = len(words) - 1
        while index >= 0:
            currentWord = words[index]
            for recordedWord in frequencyMap.keys():
                wordLength = len(currentWord)
                prefixSegment = recordedWord[:wordLength]
                suffixSegment = recordedWord[-wordLength:]
                isPrefixMatch = currentWord == prefixSegment
                isSuffixMatch = currentWord == suffixSegment
                if isPrefixMatch and isSuffixMatch:
                    totalPairs += frequencyMap[recordedWord]
            frequencyMap[currentWord] += 1
            index -= 1
        return totalPairs