class Solution:
    def maxPalindromesAfterOperations(self, words):
        def buildCounter(seq):
            outputMap = {}
            for element in seq:
                if element in outputMap:
                    outputMap[element] += 1
                else:
                    outputMap[element] = 1
            return outputMap

        combinedString = ''.join(words)
        letterCountMap = buildCounter(combinedString)

        totalPairs = 0
        totalSingles = 0
        iteratorList = list(letterCountMap.values())

        indexVar = 0
        while indexVar < len(iteratorList):
            currentCount = iteratorList[indexVar]
            dividend = currentCount // 2
            remainder = currentCount - dividend * 2
            totalPairs += dividend
            totalSingles += remainder
            indexVar += 1

        def lengthAccessor(s):
            return len(s)

        words.sort(key=lengthAccessor)

        palindromeCount = 0

        def checkAndConsumePairs(requestedPairs, availablePairs):
            return not (availablePairs < requestedPairs)

        def decrementPairs(availablePairsVar, decrementAmount):
            return availablePairsVar - decrementAmount

        for variableX in range(len(words)):
            currentWord = words[variableX]
            halfLen = (len(currentWord) - (len(currentWord) % 2)) // 2

            if checkAndConsumePairs(halfLen, totalPairs):
                totalPairs = decrementPairs(totalPairs, halfLen)
                palindromeCount += 1

        return palindromeCount