from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        occurrences = defaultdict(int)

        def loopWordsReverse(index):
            nonlocal totalPairs
            if index < 0:
                return
            currentWord = words[index]

            keysList = list(occurrences.keys())
            for key in keysList:
                lenWord = len(currentWord)
                prefixSlice = key[:lenWord]
                suffixSlice = key[-lenWord:] if lenWord <= len(key) else key
                # Condition rewritten from:
                # if not (currentWord != prefixSlice or currentWord != suffixSlice) then...
                # which is equivalent to: currentWord == prefixSlice and currentWord == suffixSlice
                if currentWord == prefixSlice and currentWord == suffixSlice:
                    totalPairs += occurrences[key]

            occurrences[currentWord] += 1
            loopWordsReverse(index - 1)

        loopWordsReverse(len(words) - 1)
        return totalPairs