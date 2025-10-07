class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        def countFrequencies(listInput):
            freqMap = {}
            posIndex = 0
            while posIndex < len(listInput):
                currentElem = listInput[posIndex]
                freqMap[currentElem] = freqMap.get(currentElem, 0) + 1
                posIndex += 1
            return freqMap

        def findMaximumValue(mapInput):
            maxVal = 0
            for key in mapInput:
                if mapInput[key] > maxVal:
                    maxVal = mapInput[key]
            return maxVal

        lengthWord = len(word)
        collectedSegments = []
        stepIter = 0

        while True:
            if stepIter >= lengthWord:
                break
            segmentSubstr = word[stepIter:stepIter + k]
            collectedSegments.append(segmentSubstr)
            stepIter += k

        frequencyCount = countFrequencies(collectedSegments)
        highestFrequency = findMaximumValue(frequencyCount)
        finalAnswer = len(collectedSegments) - highestFrequency
        return finalAnswer