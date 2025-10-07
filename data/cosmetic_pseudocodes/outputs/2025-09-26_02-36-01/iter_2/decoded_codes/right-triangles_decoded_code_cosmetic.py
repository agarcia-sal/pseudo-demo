class Solution:
    def numberOfRightTriangles(self, grid):
        rowTotal = len(grid)
        colTotal = len(grid[0])
        triangleSum = 0

        for rowIndex in range(rowTotal):
            for colIndex in range(colTotal):
                if grid[rowIndex][colIndex] == 1:
                    rowAccumulator = 0
                    colAccumulator = 0

                    for colChecker in range(colTotal):
                        if colChecker != colIndex:
                            rowAccumulator += grid[rowIndex][colChecker]

                    for rowChecker in range(rowTotal):
                        if rowChecker != rowIndex:
                            colAccumulator += grid[rowChecker][colIndex]

                    triangleSum += rowAccumulator * colAccumulator

        return triangleSum