from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        aCountAccumulator = 0
        frequencyMap = defaultdict(int)

        reversedWords = []
        idxIterator = len(words) - 1
        while idxIterator >= 0:
            reversedWords.append(words[idxIterator])
            idxIterator -= 1

        outerIndex = 0
        while outerIndex < len(reversedWords):
            currentWord = reversedWords[outerIndex]

            for recordedKey in frequencyMap:
                lengthWord = len(currentWord)
                lengthKey = len(recordedKey)

                prefixOfKey = recordedKey[:lengthWord]
                suffixOfKey = recordedKey[lengthKey - lengthWord:]

                conditionCheck1 = (currentWord == prefixOfKey)
                conditionCheck2 = (currentWord == suffixOfKey)

                if conditionCheck1 and conditionCheck2:
                    aCountAccumulator += frequencyMap[recordedKey]

            frequencyMap[currentWord] += 1
            outerIndex += 1

        return aCountAccumulator