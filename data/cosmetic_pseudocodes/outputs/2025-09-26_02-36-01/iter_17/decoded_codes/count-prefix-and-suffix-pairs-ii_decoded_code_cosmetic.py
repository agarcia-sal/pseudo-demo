from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalPairs = 0
        frequencyMap = defaultdict(int)

        def isMatching(fullString, subString):
            length_sub = len(subString)
            prefixCheck = fullString[:length_sub]
            suffixCheck = fullString[-length_sub:]
            return prefixCheck == subString and suffixCheck == subString

        index = len(words) - 1
        while index >= 0:
            currentWord = words[index]
            for key in frequencyMap:
                if isMatching(key, currentWord):
                    totalPairs += frequencyMap[key]
            frequencyMap[currentWord] += 1
            index -= 1

        return totalPairs