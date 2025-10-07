class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        totalLength = len(word)
        chunkList = []
        start = 0

        while start < totalLength:
            end = start + k
            part = word[start:end]
            chunkList.append(part)
            start += k

        frequencyMap = {}
        for element in chunkList:
            frequencyMap[element] = frequencyMap.get(element, 0) + 1

        highestFrequency = 0
        for key in frequencyMap:
            if frequencyMap[key] > highestFrequency:
                highestFrequency = frequencyMap[key]

        changesNeeded = len(chunkList) - highestFrequency
        return changesNeeded