from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        tracker = defaultdict(int)
        idx = len(words) - 1
        while idx >= 0:
            currentWord = words[idx]
            for recordedKey in tracker.keys():
                keyLength = len(recordedKey)
                currentLength = len(currentWord)
                prefixSubstr = recordedKey[:currentLength]
                suffixSubstr = recordedKey[keyLength - currentLength:]
                if currentWord == prefixSubstr and currentWord == suffixSubstr:
                    totalPairs += tracker[recordedKey]
            tracker[currentWord] += 1
            idx -= 1
        return totalPairs