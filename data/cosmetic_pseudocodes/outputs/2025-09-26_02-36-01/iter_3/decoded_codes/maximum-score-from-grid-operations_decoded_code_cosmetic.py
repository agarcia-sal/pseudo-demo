from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        size = len(grid)
        # sumGrid[col][row+1] = sum of grid[0..row][col]
        sumGrid = [[0] * (size + 1) for _ in range(size)]
        for col in range(size):
            for row in range(size):
                sumGrid[col][row + 1] = sumGrid[col][row] + grid[row][col]

        priorChosen = [0] * (size + 1)
        priorPassed = [0] * (size + 1)

        for column in range(1, size):
            chosenCurrent = [0] * (size + 1)
            skippedCurrent = [0] * (size + 1)

            for currentPos in range(size + 1):
                for previousPos in range(size + 1):
                    if currentPos > previousPos:
                        intervalScore = sumGrid[column - 1][currentPos] - sumGrid[column - 1][previousPos]

                        # Update chosenCurrent[currentPos]
                        candidateChosen = priorPassed[previousPos] + intervalScore
                        if candidateChosen > chosenCurrent[currentPos]:
                            chosenCurrent[currentPos] = candidateChosen

                        # Update skippedCurrent[currentPos]
                        candidateSkipped = priorPassed[previousPos] + intervalScore
                        if candidateSkipped > skippedCurrent[currentPos]:
                            skippedCurrent[currentPos] = candidateSkipped
                    else:
                        diffScore = sumGrid[column][previousPos] - sumGrid[column][currentPos]

                        # Update chosenCurrent[currentPos]
                        candidateChosen2 = priorChosen[previousPos] + diffScore
                        if candidateChosen2 > chosenCurrent[currentPos]:
                            chosenCurrent[currentPos] = candidateChosen2

                        # Update skippedCurrent[currentPos]
                        candidateSkipped2 = priorChosen[previousPos]
                        if candidateSkipped2 > skippedCurrent[currentPos]:
                            skippedCurrent[currentPos] = candidateSkipped2

            priorChosen = chosenCurrent
            priorPassed = skippedCurrent

        maximumValue = 0
        for val in priorChosen:
            if val > maximumValue:
                maximumValue = val

        return maximumValue