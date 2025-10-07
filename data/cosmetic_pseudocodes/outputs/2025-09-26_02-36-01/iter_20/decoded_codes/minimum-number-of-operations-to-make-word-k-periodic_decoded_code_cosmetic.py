class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        def countOccurrences(listInput):
            mapCount = {}
            idx_c = 0
            while idx_c < len(listInput):
                currentElem = listInput[idx_c]
                if currentElem in mapCount:
                    mapCount[currentElem] += 1
                else:
                    mapCount[currentElem] = 1
                idx_c += 1
            return mapCount

        def findMaxValueInMap(aMap):
            accMaxVal = 0
            for keyIterator in aMap:
                if aMap[keyIterator] > accMaxVal:
                    accMaxVal = aMap[keyIterator]
            return accMaxVal

        lenInput = 0
        listSegments = []
        posTracker = 0

        while posTracker < len(word):
            subStrSegment = ""
            limitIndex = posTracker + k
            iterIndex = posTracker
            while iterIndex < limitIndex and iterIndex < len(word):
                subStrSegment += word[iterIndex]
                iterIndex += 1
            listSegments.append(subStrSegment)
            posTracker += k

        lenInput = len(listSegments)
        occurrencesMap = countOccurrences(listSegments)
        highestFrequency = findMaxValueInMap(occurrencesMap)
        differenceResult = lenInput - highestFrequency
        return differenceResult