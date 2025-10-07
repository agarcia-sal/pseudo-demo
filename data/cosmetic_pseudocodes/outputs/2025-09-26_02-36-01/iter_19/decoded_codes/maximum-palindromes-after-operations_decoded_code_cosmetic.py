from collections import defaultdict
from typing import List

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        def ComputeCharFrequency(sequence: str) -> dict:
            tally = defaultdict(int)
            indexVar = 0
            while indexVar < len(sequence):
                currentSymbol = sequence[indexVar]
                tally[currentSymbol] += 1
                indexVar += 1
            return tally

        allJoinedStrings = ""
        idx1 = 0
        while idx1 < len(words):
            strTmp = words[idx1]
            allJoinedStrings += strTmp
            idx1 += 1

        freqMap = ComputeCharFrequency(allJoinedStrings)

        accumPairs = 0
        accumSingles = 0

        freqVals = []
        for k in freqMap:
            freqVals.append(freqMap[k])

        j = 0
        while j < len(freqVals):
            currVal = freqVals[j]
            evenComponent = currVal - (currVal % 2)
            accumPairs += evenComponent // 2
            oddComponent = currVal % 2
            accumSingles += oddComponent
            j += 1

        sortedWordsCopy = words[:]
        for a in range(len(sortedWordsCopy) - 1):
            for b in range(a + 1, len(sortedWordsCopy)):
                if len(sortedWordsCopy[a]) > len(sortedWordsCopy[b]):
                    tempSwap = sortedWordsCopy[a]
                    sortedWordsCopy[a] = sortedWordsCopy[b]
                    sortedWordsCopy[b] = tempSwap

        palindromeCount = 0
        idxW = 0
        while idxW < len(sortedWordsCopy):
            candidateWord = sortedWordsCopy[idxW]
            candidateLen = len(candidateWord)
            halfSegLen = candidateLen // 2
            if halfSegLen <= accumPairs:
                accumPairs -= halfSegLen
                palindromeCount += 1
            idxW += 1

        return palindromeCount