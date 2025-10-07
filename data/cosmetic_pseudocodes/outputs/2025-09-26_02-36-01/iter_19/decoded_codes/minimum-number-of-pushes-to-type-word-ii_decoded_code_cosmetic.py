class Solution:
    def minimumPushes(self, word: str) -> int:
        def countCharacters(text: str) -> dict:
            mapCharCounts = {}
            for idx in range(len(text)):
                currentChar = text[idx]
                if currentChar in mapCharCounts:
                    mapCharCounts[currentChar] += 1
                else:
                    mapCharCounts[currentChar] = 1
            return mapCharCounts

        mapToSort = countCharacters(word)
        listCounts = [count for count in mapToSort.values()]

        listSortedCounts = []
        while listCounts:
            maxVal = listCounts[0]
            maxIndex = 0
            for pos in range(1, len(listCounts)):
                if listCounts[pos] > maxVal:
                    maxVal = listCounts[pos]
                    maxIndex = pos
            listSortedCounts.append(maxVal)
            listCounts.pop(maxIndex)

        sumPushes = 0
        pressLevel = 1
        assignedCount = 0

        for count in listSortedCounts:
            sumPushes += count * pressLevel
            assignedCount += 1
            if assignedCount == 8:
                assignedCount = 0
                pressLevel += 1

        return sumPushes