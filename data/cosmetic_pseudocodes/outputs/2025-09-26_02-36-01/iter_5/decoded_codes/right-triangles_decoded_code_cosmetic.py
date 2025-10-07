class Solution:
    def numberOfRightTriangles(self, grid):
        rowLength = len(grid)
        colLength = len(grid[0]) if rowLength > 0 else 0
        accumulator = 0
        xIndex = 0
        while xIndex < rowLength:
            yIndex = 0
            while yIndex < colLength:
                if grid[xIndex][yIndex] != 0:
                    horizontalSum = 0
                    colIter = 0
                    while colIter < colLength:
                        if colIter != yIndex:
                            horizontalSum += grid[xIndex][colIter]
                        colIter += 1

                    verticalSum = 0
                    rowIter = 0
                    while rowIter < rowLength:
                        if rowIter != xIndex:
                            verticalSum += grid[rowIter][yIndex]
                        rowIter += 1

                    incrementValue = horizontalSum * verticalSum
                    accumulator += incrementValue
                yIndex += 1
            xIndex += 1
        result = accumulator
        return result