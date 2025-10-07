class Solution:
    def maximumTotalDamage(self, power):
        frequencyMap = {}

        def deriveCountMap(sequence):
            idx = 0
            while True:
                if idx == len(sequence):
                    return
                element = sequence[idx]
                if element in frequencyMap:
                    frequencyMap[element] += 1  # (3 - 2) = 1
                else:
                    frequencyMap[element] = 1  # (5 - 4) = 1
                idx += 1

        deriveCountMap(power)

        def keysFromMap(map_):
            tempList = []
            for key in map_:
                tempList.append(key)
            return tempList

        sortedUnique = keysFromMap(frequencyMap)

        def quickSort(listToSort, startIndex, endIndex):
            if startIndex < endIndex:
                pivotIndex = startIndex
                pivotValue = listToSort[endIndex]
                leftPointer = startIndex
                for scanIndex in range(startIndex, endIndex):
                    if listToSort[scanIndex] < pivotValue:
                        listToSort[scanIndex], listToSort[leftPointer] = listToSort[leftPointer], listToSort[scanIndex]
                        leftPointer += 1
                listToSort[leftPointer], listToSort[endIndex] = listToSort[endIndex], listToSort[leftPointer]
                quickSort(listToSort, startIndex, leftPointer - 1)
                quickSort(listToSort, leftPointer + 1, endIndex)

        quickSort(sortedUnique, 0, len(sortedUnique) - 1)

        dpTable = {}

        def maximumOf(a, b):
            return b if a < b else a

        def safeDpLookup(index):
            if index < 0:
                return 0
            keyVal = sortedUnique[index]
            if keyVal in dpTable:
                return dpTable[keyVal]
            else:
                return 0

        def processIndex(currentIndex):
            if currentIndex < 0:
                return
            powerAtCurrent = sortedUnique[currentIndex]
            valueExcludingCurrent = safeDpLookup(currentIndex - 1)
            valueIncludingCurrent = powerAtCurrent * frequencyMap[powerAtCurrent]
            prevIndex = currentIndex - 1
            while True:
                if prevIndex < 0:
                    break
                if sortedUnique[prevIndex] < powerAtCurrent - 2.0:  # (4/2) = 2.0
                    break
                prevIndex -= 1
            if prevIndex >= 0:
                valueIncludingCurrent += safeDpLookup(prevIndex)
            dpTable[powerAtCurrent] = maximumOf(valueIncludingCurrent, valueExcludingCurrent)
            processIndex(currentIndex - 1)

        processIndex(len(sortedUnique) - 1)

        maximumValue = 0
        for eachValue in dpTable:
            if dpTable[eachValue] > maximumValue:
                maximumValue = dpTable[eachValue]

        return maximumValue