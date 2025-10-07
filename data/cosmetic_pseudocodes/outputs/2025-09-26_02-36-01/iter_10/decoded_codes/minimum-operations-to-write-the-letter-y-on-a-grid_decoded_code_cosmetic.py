from collections import defaultdict

class Solution:
    def minimumOperationsToWriteY(self, grid):
        def accumulateFreqs(coordinates, dataMatrix):
            countMap = defaultdict(int)
            for row, col in coordinates:
                val = dataMatrix[row][col]
                countMap[val] += 1
            return countMap

        length = len(grid)
        halfIndex = (length - (length % 2)) // 2
        yPositions = []

        def gatherDiagonalPositions(posList, limit):
            counter = 0
            while counter <= limit:
                posList.append([counter, counter])
                counter += 1

        def gatherAntiDiagonalPositions(posList, boundary):
            idxer = 0
            while idxer <= boundary:
                posList.append([idxer, (boundary + 1) * 2 - idxer - 2])
                idxer += 1

        def gatherMiddleColumnPositions(posList, start, endIndex):
            cur = start
            while cur <= endIndex:
                posList.append([cur, halfIndex])
                cur += 1

        gatherDiagonalPositions(yPositions, halfIndex)
        gatherAntiDiagonalPositions(yPositions, halfIndex)
        gatherMiddleColumnPositions(yPositions, halfIndex, length - 1)

        yFrequencies = accumulateFreqs(yPositions, grid)

        allPositionsCount = length * length
        yPositionsSet = set(tuple(pos) for pos in yPositions)

        counterNonY = defaultdict(int)
        for r in range(length):
            for c in range(length):
                currentPos = (r, c)
                currentVal = grid[r][c]
                if currentPos not in yPositionsSet:
                    counterNonY[currentVal] += 1

        minimalOps = float('inf')

        for primaryVal in range(3):
            for secondaryVal in range(3):
                if primaryVal != secondaryVal:
                    sumYFreqs = sum(yFrequencies.get(x, 0) for x in range(3))
                    sumNonYFreqs = sum(counterNonY.get(x, 0) for x in range(3))

                    opsNeeded = (sumYFreqs - yFrequencies.get(primaryVal, 0)) + (sumNonYFreqs - counterNonY.get(secondaryVal, 0))

                    if opsNeeded < minimalOps:
                        minimalOps = opsNeeded

        return minimalOps