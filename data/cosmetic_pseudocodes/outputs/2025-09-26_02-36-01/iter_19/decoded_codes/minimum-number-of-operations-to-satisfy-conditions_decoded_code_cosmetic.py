class Solution:
    def minimumOperations(self, grid):
        count = 0
        height = len(grid)
        width = len(grid[0])

        colIdx = 0
        while colIdx < width:
            rowIdx = 0
            # Make each column non-decreasing from top to bottom
            while rowIdx < height - 1:
                if grid[rowIdx][colIdx] != grid[rowIdx + 1][colIdx]:
                    count += 1
                    grid[rowIdx + 1][colIdx] = grid[rowIdx][colIdx]
                rowIdx += 1

            idx = 0
            # Ensure adjacent columns do not contain equal elements at the same row
            while idx < height:
                if colIdx < width - 1 and grid[idx][colIdx] == grid[idx][colIdx + 1]:
                    count += 1
                    done = False
                    replacementNumber = 0
                    while replacementNumber <= 9 and not done:
                        if replacementNumber != grid[idx][colIdx]:
                            grid[idx][colIdx + 1] = replacementNumber
                            done = True
                        replacementNumber += 1
                idx += 1

            colIdx += 1

        return count