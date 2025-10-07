from collections import defaultdict

class Solution:
    def maxPalindromesAfterOperations(self, words):
        def buildCounter(textList):
            counter = defaultdict(int)
            for s in textList:
                idx = 0
                while idx < len(s):
                    keyChar = s[idx]
                    counter[keyChar] += 1
                    idx += 1
            return counter

        freqMap = buildCounter(words)
        pairSum = 0
        singleSum = 0

        valueIterator = iter(freqMap.values())

        def processNextValue():
            nonlocal pairSum, singleSum
            try:
                val = next(valueIterator)
            except StopIteration:
                return
            pairSum += val // 2
            singleSum += val - 2 * (val // 2)
            processNextValue()

        processNextValue()

        # lengthAscending returns True if length(a) > length(b), 
        # so sort so that longer words come first
        words = sorted(words, key=len, reverse=True)

        palindromeCount = 0
        indexPointer = 0

        def consumeWords():
            nonlocal indexPointer, pairSum, palindromeCount
            if indexPointer >= len(words):
                return
            currentWord = words[indexPointer]
            requiredPairs = len(currentWord) // 2
            if pairSum >= requiredPairs:
                pairSum -= requiredPairs
                palindromeCount += 1
            indexPointer += 1
            consumeWords()

        consumeWords()

        return palindromeCount