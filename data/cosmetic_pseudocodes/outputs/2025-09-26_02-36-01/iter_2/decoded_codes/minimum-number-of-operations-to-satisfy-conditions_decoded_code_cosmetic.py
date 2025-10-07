from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])
        totalOps = 0

        colIndex = 0
        while colIndex < colCount:
            rowIndex = 0
            while rowIndex < rowCount - 1:
                if grid[rowIndex][colIndex] != grid[rowIndex + 1][colIndex]:
                    totalOps += 1
                    grid[rowIndex + 1][colIndex] = grid[rowIndex][colIndex]
                rowIndex += 1

            idx = 0
            while idx < rowCount:
                if colIndex < colCount - 1 and grid[idx][colIndex] == grid[idx][colIndex + 1]:
                    totalOps += 1
                    replacementFound = False
                    candidate = 0
                    while candidate <= 9 and not replacementFound:
                        if candidate != grid[idx][colIndex]:
                            grid[idx][colIndex + 1] = candidate
                            replacementFound = True
                        candidate += 1
                idx += 1

            colIndex += 1

        return totalOps