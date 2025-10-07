class Solution:
    def minimumPushes(self, word: str) -> int:
        def countFrequency(idx: int, freqMap: dict) -> dict:
            if idx == len(word):
                return freqMap
            currentChar = word[idx]
            freqMap[currentChar] = freqMap.get(currentChar, 0) + 1
            return countFrequency(idx + 1, freqMap)

        freq_counts = countFrequency(0, {})

        def extractValues(mappings: list, valuesList: list) -> list:
            if len(mappings) == 0:
                return valuesList
            firstKey = mappings[0]
            valuesList.append(freq_counts[firstKey])
            return extractValues(mappings[1:], valuesList)

        keysArray = list(freq_counts.keys())
        countsList = extractValues(keysArray, [])

        def sortDescending(lst: list) -> list:
            if len(lst) <= 1:
                return lst
            pivot = lst[0]

            def partition(i: int, g: list, le: list):
                if i == len(lst):
                    return g, le
                if lst[i] > pivot:
                    return partition(i + 1, g + [lst[i]], le)
                else:
                    return partition(i + 1, g, le + [lst[i]])

            gPart, lePart = partition(1, [], [])
            return sortDescending(gPart) + [pivot] + sortDescending(lePart)

        sortedCounts = sortDescending(countsList)

        totalPushesAccum = 0
        currentKeyPress = 1
        keysAssignedCount = 0

        def accumulate(i: int, totalAcc: int, keyPressNum: int, assignedCount: int) -> int:
            if i == len(sortedCounts):
                return totalAcc
            val = sortedCounts[i]
            updatedTotal = totalAcc + val * keyPressNum
            updatedAssigned = assignedCount + 1
            if updatedAssigned == 8:
                return accumulate(i + 1, updatedTotal, keyPressNum + 1, 0)
            else:
                return accumulate(i + 1, updatedTotal, keyPressNum, updatedAssigned)

        result = accumulate(0, totalPushesAccum, currentKeyPress, keysAssignedCount)
        return result