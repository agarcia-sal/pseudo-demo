from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        occurrenceMap = defaultdict(int)

        def compareEnds(candidate, text):
            # Check if candidate is both prefix and suffix of text
            return candidate == text[:len(candidate)] and candidate == text[-len(candidate):]

        def processAtIndex(index):
            nonlocal totalPairs
            if index < 0:
                return
            currentWord = words[index]
            for existingKey in occurrenceMap:
                if compareEnds(currentWord, existingKey):
                    totalPairs += occurrenceMap[existingKey]
            occurrenceMap[currentWord] += 1
            processAtIndex(index - 1)

        processAtIndex(len(words) - 1)
        return totalPairs