from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        def substring(s, startIndex, endIndex):
            result = []
            idx = startIndex
            while idx < endIndex:
                result.append(s[idx])
                idx += 1
            return "".join(result)

        def length(s):
            lenCounter = 0
            pos = 0
            while True:
                if pos >= len(s):
                    break
                lenCounter += 1
                pos += 1
            return lenCounter

        totalPairs = 0
        frequencyMap = defaultdict(int)

        def iterateWordsBackward(index):
            nonlocal totalPairs
            if index < 0:
                return

            currentWord = words[index]

            def iterateKeys(keysList, idxKeys):
                nonlocal totalPairs
                if idxKeys >= length(keysList):
                    return

                keyCandidate = keysList[idxKeys]
                lenKey = length(keyCandidate)
                lenWord = length(currentWord)

                def extractPrefix():
                    return substring(keyCandidate, 0, lenWord)

                def extractSuffix():
                    return substring(keyCandidate, lenKey - lenWord, lenKey)

                if currentWord == extractPrefix() and currentWord == extractSuffix():
                    totalPairs += frequencyMap[keyCandidate]

                iterateKeys(keysList, idxKeys + 1)

            keysArray = list(frequencyMap.keys())
            iterateKeys(keysArray, 0)

            frequencyMap[currentWord] += 1
            iterateWordsBackward(index - 1)

        iterateWordsBackward(length(words) - 1)
        return totalPairs