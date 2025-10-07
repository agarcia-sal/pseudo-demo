class Solution:
    def minimumPushes(self, word: str) -> int:
        def tallyLetters(text: str) -> dict:
            frequencies = {}
            index = 0
            while index < len(text):
                currentChar = text[index]
                if currentChar not in frequencies:
                    frequencies[currentChar] = 1
                else:
                    frequencies[currentChar] += 1
                index += 1
            return frequencies

        def sortDescending(values: list) -> list:
            listCopy = values[:]
            i = 0
            while i < len(listCopy) - 1:
                j = 0
                while j < len(listCopy) - 1 - i:
                    if listCopy[j] < listCopy[j + 1]:
                        listCopy[j], listCopy[j + 1] = listCopy[j + 1], listCopy[j]
                    j += 1
                i += 1
            return listCopy

        frequencyMap = tallyLetters(word)
        freqValues = []
        for key in frequencyMap:
            freqValues.append(frequencyMap[key])
        orderedFreqs = sortDescending(freqValues)

        aggregatePushes = 0
        pressCount = 1
        assignedKeys = 0

        idx = 0
        while idx < len(orderedFreqs):
            currentCount = orderedFreqs[idx]
            aggregatePushes += currentCount * pressCount
            assignedKeys += 1
            if assignedKeys == 8:
                assignedKeys = 0
                pressCount += 1
            idx += 1

        return aggregatePushes