class Solution:
    def minimumPushes(self, word: str) -> int:
        def tallyCharacters(inputString: str) -> dict:
            accumulator = {}
            traversalIndex = 0
            while traversalIndex < len(inputString):
                currentChar = inputString[traversalIndex]
                if currentChar not in accumulator:
                    accumulator[currentChar] = 0
                accumulator[currentChar] += 1
                traversalIndex += 1
            return accumulator

        frequencyMap = tallyCharacters(word)

        countsList = []
        for key in frequencyMap:
            countsList.append(frequencyMap[key])

        def descendSort(numbersList: list) -> list:
            n = len(numbersList)
            while True:
                swapped = False
                for index in range(n - 1):
                    if numbersList[index] < numbersList[index + 1]:
                        numbersList[index], numbersList[index + 1] = numbersList[index + 1], numbersList[index]
                        swapped = True
                n -= 1
                if not swapped:
                    break
            return numbersList

        sortedCounts = descendSort(countsList)

        accumulatedPushes = 0
        pressNumber = 1
        assignedKeys = 0
        pointer = 0

        while pointer < len(sortedCounts):
            accumulatedPushes += sortedCounts[pointer] * pressNumber
            assignedKeys += 1
            if assignedKeys == 8:
                assignedKeys = 0
                pressNumber += 1
            pointer += 1

        return accumulatedPushes