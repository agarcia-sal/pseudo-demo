class Solution:
    def numberOfPairs(self, alphaList, betaList, omega):
        frequencyMap = self.buildFrequencyMap(betaList)
        totalMatches = 0

        indexA = 0
        while indexA < len(alphaList):
            currentA = alphaList[indexA]
            freqEntries = list(frequencyMap.items())

            indexB = 0
            while indexB < len(freqEntries):
                keyVal, valCount = freqEntries[indexB]
                if currentA % (keyVal * omega) == 0:
                    totalMatches += valCount
                indexB += 1

            indexA += 1

        return totalMatches

    def buildFrequencyMap(self, inputList):
        mapResult = {}
        pointer = 0
        while pointer < len(inputList):
            element = inputList[pointer]
            if element not in mapResult:
                mapResult[element] = 1
            else:
                mapResult[element] += 1
            pointer += 1
        return mapResult