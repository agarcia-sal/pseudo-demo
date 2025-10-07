class Solution:
    def minimumPushes(self, word: str) -> int:
        def tallyCharacters(inputString: str) -> dict:
            countsMap = {}
            position = 0
            lengthLimit = len(inputString)
            while position < lengthLimit:
                character = inputString[position]
                if character not in countsMap:
                    countsMap[character] = 1
                else:
                    countsMap[character] += 1
                position += 1
            return countsMap

        letterCounts = tallyCharacters(word)
        countsList = []
        for letterKey in letterCounts:
            countsList.append(letterCounts[letterKey])

        # Selection sort in descending order
        countsLength = len(countsList)
        index = 0
        while index < countsLength:
            maxIndex = index
            scanIndex = index + 1
            while scanIndex < countsLength:
                if countsList[scanIndex] > countsList[maxIndex]:
                    maxIndex = scanIndex
                scanIndex += 1
            countsList[index], countsList[maxIndex] = countsList[maxIndex], countsList[index]
            index += 1
        descendingCounts = countsList

        cumulativePushes = 0
        strokesPerKey = 1
        assignedKeysCounter = 0
        positionCounter = 0
        lengthDescending = len(descendingCounts)
        while positionCounter < lengthDescending:
            cumulativePushes += descendingCounts[positionCounter] * strokesPerKey
            assignedKeysCounter += 1
            if not (assignedKeysCounter < 8):
                assignedKeysCounter = 0
                strokesPerKey += 1
            positionCounter += 1

        return cumulativePushes