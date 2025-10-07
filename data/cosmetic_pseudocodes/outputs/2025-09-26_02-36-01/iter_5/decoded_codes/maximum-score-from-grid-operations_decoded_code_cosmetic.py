class Solution:
    def maximumScore(self, grid):
        lengthValue = len(grid)
        prefixMatrix = [[0] * (lengthValue + 1) for _ in range(lengthValue + 1)]
        previousSelected = [0] * (lengthValue + 1)
        previousSkipped = [0] * (lengthValue + 1)

        def fillPrefix(currentColumn, currentRow):
            if currentColumn < lengthValue:
                if currentRow < lengthValue:
                    computedSum = prefixMatrix[currentColumn][currentRow] + grid[currentRow][currentColumn]
                    prefixMatrix[currentColumn][currentRow + 1] = computedSum
                    fillPrefix(currentColumn, currentRow + 1)
                else:
                    fillPrefix(currentColumn + 1, 0)

        fillPrefix(0, 0)

        def processColumn(colIndex, selectedPrev, skippedPrev):
            if colIndex == lengthValue:
                return selectedPrev, skippedPrev

            selectedCurrent = [0] * (lengthValue + 1)
            skippedCurrent = [0] * (lengthValue + 1)

            def processCurr(currIndex):
                if currIndex > lengthValue:
                    return

                def iteratePrev(prevIndex):
                    if prevIndex > lengthValue:
                        return

                    if currIndex > prevIndex:
                        segmentScore = prefixMatrix[colIndex - 1][currIndex] - prefixMatrix[colIndex - 1][prevIndex]
                        selectedCurrent[currIndex] = max(selectedCurrent[currIndex], skippedPrev[prevIndex] + segmentScore)
                        skippedCurrent[currIndex] = max(skippedCurrent[currIndex], skippedPrev[prevIndex] + segmentScore)
                    else:
                        segmentScore = prefixMatrix[colIndex][prevIndex] - prefixMatrix[colIndex][currIndex]
                        selectedCurrent[currIndex] = max(selectedCurrent[currIndex], selectedPrev[prevIndex] + segmentScore)
                        skippedCurrent[currIndex] = max(skippedCurrent[currIndex], selectedPrev[prevIndex])

                    iteratePrev(prevIndex + 1)

                iteratePrev(0)
                processCurr(currIndex + 1)

            processCurr(0)

            return processColumn(colIndex + 1, selectedCurrent, skippedCurrent)

        finalSelected, finalSkipped = processColumn(1, previousSelected, previousSkipped)

        maxResult = 0
        for val in finalSelected:
            if val > maxResult:
                maxResult = val

        return maxResult