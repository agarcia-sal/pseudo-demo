from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        cumulative = [[0] * (m + 1) for _ in range(m)]
        earlierSelected = [0] * (m + 1)
        earlierSkipped = [0] * (m + 1)

        # Compute cumulative sums for each row
        for rowIndex in range(m):
            for colIndex in range(m):
                cumulative[rowIndex][colIndex + 1] = cumulative[rowIndex][colIndex] + grid[rowIndex][colIndex]

        lineNumber = 1
        while lineNumber <= m - 1:
            currentSelected = [0] * (m + 1)
            currentSkipped = [0] * (m + 1)

            for currentPos in range(m + 1):
                for previousPos in range(m + 1):
                    if currentPos > previousPos:
                        segmentScore = cumulative[lineNumber][currentPos - 1] - cumulative[lineNumber][previousPos]
                        candidateSelected = currentSelected[currentPos]
                        candidateSkipped = currentSkipped[currentPos]

                        newSelected = earlierSkipped[previousPos] + segmentScore
                        newSkipped = earlierSkipped[previousPos] + segmentScore

                        if newSelected > candidateSelected:
                            currentSelected[currentPos] = newSelected
                        else:
                            currentSelected[currentPos] = candidateSelected

                        if newSkipped > candidateSkipped:
                            currentSkipped[currentPos] = newSkipped
                        else:
                            currentSkipped[currentPos] = candidateSkipped
                    else:
                        segmentScore = cumulative[lineNumber][previousPos] - cumulative[lineNumber][currentPos]
                        candidateSelected = currentSelected[currentPos]
                        candidateSkipped = currentSkipped[currentPos]

                        newSelected = earlierSelected[previousPos] + segmentScore
                        newSkippedOpt = earlierSelected[previousPos]

                        if newSelected > candidateSelected:
                            currentSelected[currentPos] = newSelected
                        else:
                            currentSelected[currentPos] = candidateSelected

                        if newSkippedOpt > candidateSkipped:
                            currentSkipped[currentPos] = newSkippedOpt
                        else:
                            currentSkipped[currentPos] = candidateSkipped

            earlierSelected = currentSelected
            earlierSkipped = currentSkipped
            lineNumber += 1

        answer = earlierSelected[0]
        for val in earlierSelected[1:]:
            if val > answer:
                answer = val

        return answer