class Solution:
    def minimumOperationsToWriteY(self, grid):
        lengthGrid = len(grid)
        midPoint = lengthGrid // 2
        yPositions = set()

        # Adds positions along the main diagonal from (0,0) to (midPoint, midPoint)
        def addDiagonal(idx, limit, container):
            if idx > limit:
                return
            container.add((idx, idx))
            addDiagonal(idx + 1, limit, container)

        addDiagonal(0, midPoint, yPositions)

        # Adds positions along the anti-diagonal from (0, lengthGrid-1) to (midPoint, lengthGrid - midPoint -1)
        def addAntiDiagonal(idx, limit, container):
            if idx > limit:
                return
            container.add((idx, (lengthGrid - idx) - 1))
            addAntiDiagonal(idx + 1, limit, container)

        addAntiDiagonal(0, midPoint, yPositions)

        # Adds vertical line positions from (midPoint, midPoint) to (lengthGrid -1, midPoint)
        def addVerticalSlice(idx, limit, fixedCol, container):
            if idx > limit:
                return
            container.add((idx, fixedCol))
            addVerticalSlice(idx + 1, limit, fixedCol, container)

        addVerticalSlice(midPoint, lengthGrid - 1, midPoint, yPositions)

        # Counts occurrences of values 0, 1, 2 at specified positions in matrix
        def countValuesAtPositions(matrix, positions):
            totalCounts = {0: 0, 1: 0, 2: 0}
            for rowIdx, colIdx in positions:
                val = matrix[rowIdx][colIdx]
                totalCounts[val] += 1
            return totalCounts

        yCountMap = countValuesAtPositions(grid, yPositions)

        # Counts occurrences of values 0,1,2 outside specified positions in matrix
        def countValuesOutsidePositions(matrix, positions):
            countsMap = {0: 0, 1: 0, 2: 0}
            for rowIdx in range(lengthGrid):
                for colIdx in range(lengthGrid):
                    if (rowIdx, colIdx) not in positions:
                        entryVal = matrix[rowIdx][colIdx]
                        countsMap[entryVal] += 1
            return countsMap

        nonYCountMap = countValuesOutsidePositions(grid, yPositions)

        minimalOps = float('inf')

        # Recursive function to iterate over yVal in 0..2
        def productLoopY(yVal, result):
            if yVal > 2:
                return result

            # Recursive function to iterate over nonYVal in 0..2
            def productLoopNonY(nonYVal, currentResult):
                if nonYVal > 2:
                    return currentResult
                if yVal != nonYVal:
                    sumY = sum(yCountMap[key] for key in range(3))
                    sumNonY = sum(nonYCountMap[key] for key in range(3))
                    operationCount = (sumY - yCountMap[yVal]) + (sumNonY - nonYCountMap[nonYVal])
                    if operationCount < currentResult:
                        currentResult = operationCount
                return productLoopNonY(nonYVal + 1, currentResult)

            updatedResult = productLoopNonY(0, result)
            return productLoopY(yVal + 1, updatedResult)

        minimalOps = productLoopY(0, minimalOps)

        return minimalOps