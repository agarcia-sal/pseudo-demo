from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        frequencyMap = defaultdict(int)

        def checkAllKeysRecursively(keysList, idx, currentWord):
            if idx >= len(keysList):
                return 0
            currentKey = keysList[idx]
            partialCount = 0
            lenCurrentWord = len(currentWord)
            lenCurrentKey = len(currentKey)
            if (lenCurrentWord <= lenCurrentKey and
                currentWord == currentKey[:lenCurrentWord] and
                currentWord == currentKey[lenCurrentKey - lenCurrentWord:]):
                partialCount = frequencyMap[currentKey]
            return partialCount + checkAllKeysRecursively(keysList, idx + 1, currentWord)

        def processWordsRecursively(idx):
            if idx < 0:
                return 0
            wordNow = words[idx]
            keysList = list(frequencyMap.keys())
            countForThis = checkAllKeysRecursively(keysList, 0, wordNow)
            frequencyMap[wordNow] += 1
            return countForThis + processWordsRecursively(idx - 1)

        totalPairs = processWordsRecursively(len(words) - 1)
        return totalPairs