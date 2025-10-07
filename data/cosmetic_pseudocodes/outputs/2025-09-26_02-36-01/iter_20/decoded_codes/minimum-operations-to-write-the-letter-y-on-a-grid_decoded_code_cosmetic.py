class Solution:
    def minimumOperationsToWriteY(self, grid):
        lengthVar = len(grid)
        midIndex = lengthVar // 2
        coordCollection = set()

        iterVar = 0
        while iterVar <= midIndex:
            coordCollection.add((iterVar, iterVar))
            iterVar += 1

        auxIndex = 0
        while auxIndex <= midIndex:
            coordCollection.add((auxIndex, lengthVar - auxIndex - 1))
            auxIndex += 1

        kIndex = midIndex
        while kIndex <= lengthVar - 1:
            coordCollection.add((kIndex, midIndex))
            kIndex += 1

        def countFrequencies(posSet, matrix):
            freqDict = {}
            for rowCounter in range(len(matrix)):
                for colCounter in range(len(matrix[rowCounter])):
                    currentCoord = (rowCounter, colCounter)
                    if currentCoord in posSet:
                        currentVal = matrix[rowCounter][colCounter]
                        freqDict[currentVal] = freqDict.get(currentVal, 0) + 1
            return freqDict

        def countExclusionFrequencies(posSet, matrix):
            freqMap = {}
            for rIndex in range(len(matrix)):
                for cIndex in range(len(matrix[rIndex])):
                    posRef = (rIndex, cIndex)
                    if posRef not in posSet:
                        valueRef = matrix[rIndex][cIndex]
                        freqMap[valueRef] = freqMap.get(valueRef, 0) + 1
            return freqMap

        countingY = countFrequencies(coordCollection, grid)
        countingNonY = countExclusionFrequencies(coordCollection, grid)
        infiniteVal = float('inf')
        currentMin = infiniteVal

        def totalFrequency(freqMap):
            return sum(freqMap.values())

        outerLoopVar = 0
        while outerLoopVar <= 2:
            innerLoopVar = 0
            while innerLoopVar <= 2:
                if outerLoopVar != innerLoopVar:
                    sumAllY = totalFrequency(countingY)
                    freqYAtVal = countingY.get(outerLoopVar, 0)
                    sumAllNonY = totalFrequency(countingNonY)
                    freqNonYAtVal = countingNonY.get(innerLoopVar, 0)
                    opVal = (sumAllY - freqYAtVal) + (sumAllNonY - freqNonYAtVal)
                    if opVal < currentMin:
                        currentMin = opVal
                innerLoopVar += 1
            outerLoopVar += 1

        return currentMin