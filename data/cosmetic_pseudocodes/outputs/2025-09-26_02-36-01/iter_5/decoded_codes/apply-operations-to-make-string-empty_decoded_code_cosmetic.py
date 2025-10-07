class Solution:
    def lastNonEmptyString(self, inputString: str) -> str:
        def gatherFrequencies(index: int, freqMap: dict) -> dict:
            if index < 0:
                return freqMap
            else:
                currentChar = inputString[index]
                freqMap[currentChar] = freqMap.get(currentChar, 0) + 1
                return gatherFrequencies(index - 1, freqMap)

        def findMaxValue(freqDictionary: dict) -> int:
            maxVal = 0
            for key in freqDictionary:
                candidate = freqDictionary[key]
                if candidate > maxVal:
                    maxVal = candidate
            return maxVal

        def accumulateResults(position: int, charsSet: set, collected: list) -> list:
            if position == len(inputString):
                return collected
            else:
                currentElement = inputString[position]
                if currentElement in charsSet:
                    collected.append(currentElement)
                    charsSet.remove(currentElement)
                return accumulateResults(position + 1, charsSet, collected)

        freqCounter = gatherFrequencies(len(inputString) - 1, {})
        peakFreq = findMaxValue(freqCounter)

        setOfMaxChars = set()
        for elementKey in freqCounter:
            if freqCounter[elementKey] == peakFreq:
                setOfMaxChars.add(elementKey)

        collectedChars = accumulateResults(0, setOfMaxChars, [])

        reversedString = ''
        for i in range(len(collectedChars) - 1, -1, -1):
            reversedString += collectedChars[i]

        return reversedString