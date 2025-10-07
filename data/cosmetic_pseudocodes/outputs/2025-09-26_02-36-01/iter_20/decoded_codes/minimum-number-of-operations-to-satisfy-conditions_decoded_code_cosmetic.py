class Solution:
    def minimumOperations(self, grid):
        def replicateValue(source, target, index):
            while index < len(source) - 1:
                if source[index][target] != source[index + 1][target]:
                    source[index + 1][target] = source[index][target]
                    return 1
                index += 1
            return 0

        def substituteDifferentValue(grid, row, col, maxVal):
            if col < maxVal - 1 and grid[row][col] == grid[row][col + 1]:
                for candidate in range(10):
                    if candidate != grid[row][col]:
                        grid[row][col + 1] = candidate
                        return 1
                return 0
            return 0

        rows = len(grid)
        cols = len(grid[0])
        countOperations = 0
        columnIndex = 0

        while columnIndex < cols:
            rowIndex = 0
            while rowIndex < rows - 1:
                countOperations += replicateValue(grid, columnIndex, rowIndex)
                rowIndex += 1

            rowCheck = 0
            while rowCheck < rows:
                countOperations += substituteDifferentValue(grid, rowCheck, columnIndex, cols)
                rowCheck += 1

            columnIndex += 1

        return countOperations