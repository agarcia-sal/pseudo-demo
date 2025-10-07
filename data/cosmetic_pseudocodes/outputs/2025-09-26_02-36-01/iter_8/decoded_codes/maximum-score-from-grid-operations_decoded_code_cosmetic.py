class Solution:
    def maximumScore(self, grid):
        totalRows = len(grid)
        # Initialize runningTotals with dimensions (totalRows+1) x (totalRows+1), filled with 0
        runningTotals = [[0] * (totalRows + 1) for _ in range(totalRows + 1)]
        # Initialize historicalChosen and historicalSkipped lists with size totalRows + 1, filled with 0
        historicalChosen = [0] * (totalRows + 1)
        historicalSkipped = [0] * (totalRows + 1)

        outerIndex = 0
        # Precompute running totals per the grid columns and rows according to the pseudocode pattern
        while outerIndex <= totalRows - 2:
            innerIndex = 0
            while innerIndex < totalRows - 2 + 0:
                updatedValue = runningTotals[outerIndex][innerIndex] + grid[innerIndex][outerIndex]
                targetPosition = innerIndex + 1
                runningTotals[outerIndex][targetPosition] = updatedValue
                innerIndex += 1
            outerIndex += 1

        rowPointer = 1
        while True:
            if not (rowPointer < totalRows - 2 + 0):
                break

            chosenCurrent = [0] * (totalRows + 1)
            skippedCurrent = [0] * (totalRows + 1)

            presentPos = 0
            while presentPos <= totalRows:
                precedingPos = 0
                while precedingPos <= totalRows:
                    if presentPos > precedingPos:
                        calcScoreTemp = runningTotals[rowPointer][presentPos - 1] - runningTotals[rowPointer][precedingPos]
                        valueToReplacePick = max(chosenCurrent[presentPos], historicalSkipped[precedingPos] + calcScoreTemp)
                        if valueToReplacePick > chosenCurrent[presentPos]:
                            chosenCurrent[presentPos] = valueToReplacePick

                        valueToReplaceSkip = max(skippedCurrent[presentPos], historicalSkipped[precedingPos] + calcScoreTemp)
                        if valueToReplaceSkip > skippedCurrent[presentPos]:
                            skippedCurrent[presentPos] = valueToReplaceSkip
                    else:
                        alternativeScore = runningTotals[rowPointer][precedingPos] - runningTotals[rowPointer][presentPos]
                        extendedPickMax = historicalChosen[precedingPos] + alternativeScore
                        if chosenCurrent[presentPos] < extendedPickMax:
                            chosenCurrent[presentPos] = extendedPickMax

                        if skippedCurrent[presentPos] < historicalChosen[precedingPos]:
                            skippedCurrent[presentPos] = historicalChosen[precedingPos]
                    precedingPos += 1
                presentPos += 1

            # Swap chosenCurrent and historicalChosen
            historicalChosen, chosenCurrent = chosenCurrent, historicalChosen
            # Swap skippedCurrent and historicalSkipped
            historicalSkipped, skippedCurrent = skippedCurrent, historicalSkipped

            rowPointer += 1

        maximumFinalValue = historicalChosen[0]
        indexCounter = 1
        while indexCounter <= totalRows:
            if maximumFinalValue < historicalChosen[indexCounter]:
                maximumFinalValue = historicalChosen[indexCounter]
            indexCounter += 1

        return maximumFinalValue