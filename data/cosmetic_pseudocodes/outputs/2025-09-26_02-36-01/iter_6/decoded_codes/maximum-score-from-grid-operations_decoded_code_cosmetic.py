class Solution:
    def maximumScore(self, grid):
        lengthGrid = len(grid)
        # Initialize sumPrefix as 2D list of zeros with dimension (lengthGrid + 1) x (lengthGrid + 1)
        sumPrefix = [[0] * (lengthGrid + 1) for _ in range(lengthGrid + 1)]
        # Initialize lastPickArray and lastSkipArray with length lengthGrid + 1
        lastPickArray = [0] * (lengthGrid + 1)
        lastSkipArray = [0] * (lengthGrid + 1)

        colIndex = 0
        while colIndex < lengthGrid:
            rowIndex = 0
            while rowIndex < lengthGrid:
                updatedVal = sumPrefix[colIndex][rowIndex] + grid[rowIndex][colIndex]
                sumPrefix[colIndex][rowIndex + 1] = updatedVal
                rowIndex += 1
            colIndex += 1

        colPos = 1
        while colPos < lengthGrid:
            currentPickList = [0] * (lengthGrid + 1)
            currentSkipList = [0] * (lengthGrid + 1)

            currIndex = 0
            while True:
                if currIndex > lengthGrid:
                    break
                prevIndex = 0
                while True:
                    if prevIndex > lengthGrid:
                        break
                    if not (currIndex <= prevIndex):
                        tempScore1 = sumPrefix[colPos - 1][currIndex] - sumPrefix[colPos - 1][prevIndex]
                        val1 = currentPickList[currIndex]
                        val2 = lastSkipArray[prevIndex] + tempScore1
                        if val1 < val2:
                            currentPickList[currIndex] = val2

                        val3 = currentSkipList[currIndex]
                        val4 = lastSkipArray[prevIndex] + tempScore1
                        if val3 < val4:
                            currentSkipList[currIndex] = val4
                    else:
                        tempScore2 = sumPrefix[colPos][prevIndex] - sumPrefix[colPos][currIndex]
                        val5 = currentPickList[currIndex]
                        val6 = lastPickArray[prevIndex] + tempScore2
                        if val5 < val6:
                            currentPickList[currIndex] = val6

                        val7 = currentSkipList[currIndex]
                        val8 = lastPickArray[prevIndex]
                        if val7 < val8:
                            currentSkipList[currIndex] = val8
                    prevIndex += 1
                currIndex += 1

            lastPickArray = currentPickList
            lastSkipArray = currentSkipList

            colPos += 1

        maxScoreFound = 0
        idxWalker = 0
        while idxWalker < len(lastPickArray):
            if lastPickArray[idxWalker] > maxScoreFound:
                maxScoreFound = lastPickArray[idxWalker]
            idxWalker += 1
        return maxScoreFound