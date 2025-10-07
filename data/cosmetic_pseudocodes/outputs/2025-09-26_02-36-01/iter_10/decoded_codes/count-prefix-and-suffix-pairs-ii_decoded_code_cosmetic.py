from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        totalMatches = 0
        frequencyMap = defaultdict(int)

        def checkEdges(baseStr, cmpStr):
            lengthA = len(cmpStr)
            lengthB = len(baseStr)
            return (cmpStr == baseStr[:lengthA]) and (cmpStr == baseStr[lengthB - lengthA:])

        def iterateKeys(keysList, currentWord, accumulator):
            if not keysList:
                return accumulator
            currentKey, *tailKeys = keysList
            if checkEdges(currentWord, currentKey):
                return iterateKeys(tailKeys, currentWord, accumulator + frequencyMap[currentKey])
            else:
                return iterateKeys(tailKeys, currentWord, accumulator)

        def processWords(index):
            nonlocal totalMatches
            if index < 0:
                return
            wordAtIndex = words[index]
            keysSnapshot = list(frequencyMap.keys())
            totalMatches += iterateKeys(keysSnapshot, wordAtIndex, 0)
            frequencyMap[wordAtIndex] += 1
            processWords(index - 1)

        processWords(len(words) - 1)
        return totalMatches