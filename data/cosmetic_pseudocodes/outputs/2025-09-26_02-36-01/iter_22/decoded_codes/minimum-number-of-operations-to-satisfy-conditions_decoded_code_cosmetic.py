from typing import List

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        operations = 0

        col = 0
        while col < cols:
            row = 0
            while row < rows - 1:
                if grid[row][col] != grid[row + 1][col]:
                    operations += 1
                    grid[row + 1][col] = grid[row][col]
                row += 1

            row = 0
            while row < rows:
                if col < cols - 1 and grid[row][col] == grid[row][col + 1]:
                    operations += 1
                    for candidate in range(10):
                        if candidate != grid[row][col]:
                            grid[row][col + 1] = candidate
                            break
                row += 1

            col += 1

        return operations