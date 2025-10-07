from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        totalOps = 0

        for col in range(cols):
            for row in range(rows - 1):
                if grid[row][col] != grid[row + 1][col]:
                    totalOps += 1
                    grid[row + 1][col] = grid[row][col]

            if col < cols - 1:
                for row in range(rows):
                    if grid[row][col] == grid[row][col + 1]:
                        totalOps += 1
                        for candidateVal in range(10):
                            if candidateVal != grid[row][col]:
                                grid[row][col + 1] = candidateVal
                                break

        return totalOps