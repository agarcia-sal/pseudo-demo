class Solution:
    def minimumOperationsToWriteY(self, grid):
        lengthGrid = len(grid)
        midPoint = lengthGrid // 2
        positionsInY = set()

        idx = 0
        while idx <= midPoint:
            positionsInY.add((idx, idx))
            idx += 1

        idx = 0
        while idx <= midPoint:
            revIndex = lengthGrid - idx - 1
            positionsInY.add((idx, revIndex))
            idx += 1

        idx = midPoint
        while idx <= lengthGrid - 1:
            positionsInY.add((idx, midPoint))
            idx += 1

        yPositionsCount = {}
        nonYPositionsCount = {}

        rowPos = 0
        while rowPos < lengthGrid:
            colPos = 0
            while colPos < lengthGrid:
                currentValue = grid[rowPos][colPos]
                coordPair = (rowPos, colPos)
                if coordPair in positionsInY:
                    yPositionsCount[currentValue] = yPositionsCount.get(currentValue, 0) + 1
                else:
                    nonYPositionsCount[currentValue] = nonYPositionsCount.get(currentValue, 0) + 1
                colPos += 1
            rowPos += 1

        minimalOperations = float('inf')

        yCandidate = 0
        while yCandidate <= 2:
            nonYCandidate = 0
            while nonYCandidate <= 2:
                if yCandidate != nonYCandidate:
                    totalYCount = sum(yPositionsCount.values())
                    yCandidateCount = yPositionsCount.get(yCandidate, 0)

                    totalNonYCount = sum(nonYPositionsCount.values())
                    nonYCandidateCount = nonYPositionsCount.get(nonYCandidate, 0)

                    currentOperations = (totalYCount - yCandidateCount) + (totalNonYCount - nonYCandidateCount)

                    if currentOperations < minimalOperations:
                        minimalOperations = currentOperations
                nonYCandidate += 1
            yCandidate += 1

        return minimalOperations