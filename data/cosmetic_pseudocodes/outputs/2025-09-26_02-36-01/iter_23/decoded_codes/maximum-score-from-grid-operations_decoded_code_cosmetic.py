class Solution:
    def maximumScore(self, grid):
        def calculatePrefixSums(matrix, dimension, accumulator):
            def fillRow(colIndex, rowIndex):
                if rowIndex < dimension:
                    accVal = accumulator[colIndex][rowIndex + 1] + matrix[rowIndex][colIndex]
                    accumulator[colIndex][rowIndex + 1] = accVal
                    fillRow(colIndex, rowIndex + 1)

            def processColumns(currCol):
                if currCol < dimension:
                    fillRow(currCol, 0)
                    processColumns(currCol + 1)

            processColumns(0)

        szA = len(grid)
        prefixGrid = [[0] * (szA + 1) for _ in range(szA + 1)]
        previousSelection = [0] * (szA + 1)
        previousOmission = [0] * (szA + 1)

        calculatePrefixSums(grid, szA, prefixGrid)

        def iterateRows(rowIndex):
            if rowIndex < szA:
                currentSelection = [0] * (szA + 1)
                currentOmission = [0] * (szA + 1)

                def outerLoop(currIndex):
                    if currIndex <= szA:
                        def innerLoop(prevIndex):
                            if prevIndex <= szA:
                                if currIndex > prevIndex:
                                    computedScore = prefixGrid[rowIndex][currIndex - 1] - prefixGrid[rowIndex][prevIndex]
                                    val_selection = previousOmission[prevIndex] + computedScore
                                    if val_selection > currentSelection[currIndex]:
                                        currentSelection[currIndex] = val_selection
                                    val_omission = previousOmission[prevIndex] + computedScore
                                    if val_omission > currentOmission[currIndex]:
                                        currentOmission[currIndex] = val_omission
                                else:
                                    computedScore = prefixGrid[rowIndex][prevIndex] - prefixGrid[rowIndex][currIndex]
                                    val_selection = previousSelection[prevIndex] + computedScore
                                    if val_selection > currentSelection[currIndex]:
                                        currentSelection[currIndex] = val_selection
                                    val_omission = previousSelection[prevIndex]
                                    if val_omission > currentOmission[currIndex]:
                                        currentOmission[currIndex] = val_omission
                                innerLoop(prevIndex + 1)

                        innerLoop(0)
                        outerLoop(currIndex + 1)

                outerLoop(0)
                nonlocal previousSelection, previousOmission
                previousSelection = currentSelection
                previousOmission = currentOmission
                iterateRows(rowIndex + 1)

        iterateRows(1)

        def findMaxValue(sequence, index, bestSoFar):
            if index < len(sequence):
                candidate = sequence[index]
                newBest = candidate if candidate > bestSoFar else bestSoFar
                return findMaxValue(sequence, index + 1, newBest)
            else:
                return bestSoFar

        return findMaxValue(previousSelection, 0, -2)