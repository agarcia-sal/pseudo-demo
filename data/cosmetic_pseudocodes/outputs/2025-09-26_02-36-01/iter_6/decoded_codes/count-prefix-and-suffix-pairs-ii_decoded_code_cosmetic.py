from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        occurrenceMap = defaultdict(int)

        def comparePrefixSuffix(candidate, reference):
            candidateLength = len(candidate)
            prefixSegment = reference[:candidateLength]
            suffixSegment = reference[len(reference) - candidateLength:]
            return candidate == prefixSegment and candidate == suffixSegment

        def iterateOverIndicesDescending(idx):
            nonlocal totalPairs
            if idx < 0:
                return
            currentWord = words[idx]
            for mapKey in occurrenceMap:
                if comparePrefixSuffix(currentWord, mapKey):
                    totalPairs += occurrenceMap[mapKey]
            occurrenceMap[currentWord] += 1
            iterateOverIndicesDescending(idx - 1)

        iterateOverIndicesDescending(len(words) - 1)
        return totalPairs