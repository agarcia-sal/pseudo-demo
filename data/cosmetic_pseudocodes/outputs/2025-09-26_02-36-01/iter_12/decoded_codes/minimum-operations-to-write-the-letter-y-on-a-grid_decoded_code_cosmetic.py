class Solution:
    def minimumOperationsToWriteY(self, grid):
        def CalculateSum(collection):
            totalSum = 0
            iterator = 0
            while iterator < len(collection):
                totalSum += collection[iterator]
                iterator += 1
            return totalSum

        def IsInSet(pair, container):
            exists = False
            position = 0
            while position < len(container):
                if container[position][0] == pair[0] and container[position][1] == pair[1]:
                    exists = True
                    break
                position += 1
            return exists

        sizeGrid = len(grid)
        middleIndex = sizeGrid // 2
        designatedCells = []

        indexA = 0
        while indexA <= middleIndex:
            designatedCells.append([indexA, indexA])
            indexA += 1

        indexB = 0
        while True:
            designatedCells.append([indexB, sizeGrid - indexB - 1])
            indexB += 1
            if indexB > middleIndex:
                break

        indexC = middleIndex
        while indexC <= sizeGrid - 1:
            designatedCells.append([indexC, middleIndex])
            indexC += 1

        tallyY = {}
        tallyNotY = {}

        r = 0
        while r < sizeGrid:
            c = 0
            while c < sizeGrid:
                cellValue = grid[r][c]
                cellCoordinates = [r, c]
                if IsInSet(cellCoordinates, designatedCells):
                    if cellValue not in tallyY:
                        tallyY[cellValue] = 0
                    tallyY[cellValue] += 1
                else:
                    if cellValue not in tallyNotY:
                        tallyNotY[cellValue] = 0
                    tallyNotY[cellValue] += 1
                c += 1
            r += 1

        infinitePositive = float('inf')
        minimalOperations = infinitePositive

        possibleYValue = 0
        while possibleYValue <= 2:
            possibleNotYValue = 0
            while possibleNotYValue <= 2:
                if possibleYValue != possibleNotYValue:
                    totalY = 0
                    if len(tallyY) > 0:
                        # sum all values in tallyY
                        totalY = sum(tallyY.values())
                    totalNotY = 0
                    if len(tallyNotY) > 0:
                        # sum all values in tallyNotY
                        totalNotY = sum(tallyNotY.values())

                    operationsRequired = (
                        totalY - tallyY.get(possibleYValue, 0)
                        + totalNotY - tallyNotY.get(possibleNotYValue, 0)
                    )
                    if operationsRequired < minimalOperations:
                        minimalOperations = operationsRequired
                possibleNotYValue += 1
            possibleYValue += 1

        return minimalOperations