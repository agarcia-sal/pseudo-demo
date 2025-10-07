from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        totalLength = len(word)
        segmentList = []
        position = 0
        while position < totalLength:
            upperBound = position + k - 1
            sliceEnd = upperBound if upperBound < totalLength else totalLength - 1
            segmentList.append(word[position : sliceEnd + 1])
            position += k
        frequencyMap = Counter(segmentList)
        greatestFrequency = max(frequencyMap.values()) if frequencyMap else 0
        totalSegments = len(segmentList)
        operationsNeeded = totalSegments - greatestFrequency
        return operationsNeeded