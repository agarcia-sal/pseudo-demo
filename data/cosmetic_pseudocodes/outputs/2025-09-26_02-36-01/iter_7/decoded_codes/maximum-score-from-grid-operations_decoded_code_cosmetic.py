class Solution:
    def maximumScore(self, grid):
        size = len(grid)
        prefix = [[0] * (size + 1) for _ in range(size + 1)]
        oldChosen = [0] * (size + 1)
        oldIgnored = [0] * (size + 1)

        # Compute prefix sums for each row
        for rowIndex in range(size):
            for colIndex in range(size):
                prefix[colIndex + 1][rowIndex] = prefix[colIndex][rowIndex] + grid[rowIndex][colIndex]

        lineIndex = 1
        while lineIndex < size:
            newChosen = [0] * (size + 1)
            newIgnored = [0] * (size + 1)

            currentPos = 0
            while currentPos <= size:
                previousPos = 0
                while previousPos <= size:
                    if currentPos > previousPos:
                        segmentScore = prefix[currentPos][lineIndex - 1] - prefix[previousPos][lineIndex - 1]
                        newChosen[currentPos] = max(newChosen[currentPos], oldIgnored[previousPos] + segmentScore)
                        newIgnored[currentPos] = max(newIgnored[currentPos], oldIgnored[previousPos] + segmentScore)
                    else:
                        segmentScore = prefix[previousPos][lineIndex] - prefix[currentPos][lineIndex]
                        newChosen[currentPos] = max(newChosen[currentPos], oldChosen[previousPos] + segmentScore)
                        newIgnored[currentPos] = max(newIgnored[currentPos], oldChosen[previousPos])
                    previousPos += 1
                currentPos += 1

            oldChosen = newChosen
            oldIgnored = newIgnored
            lineIndex += 1

        maximumValue = -10 ** 10  # sufficiently low initial value
        for indexVar in range(size + 1):
            if oldChosen[indexVar] > maximumValue:
                maximumValue = oldChosen[indexVar]

        return maximumValue