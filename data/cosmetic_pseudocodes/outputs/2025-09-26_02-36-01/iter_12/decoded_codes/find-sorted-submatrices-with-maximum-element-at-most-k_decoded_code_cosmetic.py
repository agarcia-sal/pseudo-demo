class Solution:
    def countSubmatrices(self, grid, k):
        def anyElementExceedsLimit(mat):
            def checkRowElements(row, limit):
                idx = 0
                while idx < len(row):
                    if row[idx] > limit:
                        return True
                    idx += 1
                return False

            r = 0
            while r < len(mat):
                if checkRowElements(mat[r], k):
                    return True
                r += 1
            return False

        def hasViolationInOrder(mat):
            rowIdx = 0
            while rowIdx < len(mat):
                colIdx = 1
                while colIdx < len(mat[rowIdx]):
                    if mat[rowIdx][colIdx] > mat[rowIdx][colIdx - 1]:
                        return True
                    colIdx += 1
                rowIdx += 1
            return False

        height = 0
        while height < len(grid):
            height += 1
        width = 0
        while width < len(grid[0]):
            width += 1

        totalMatches = 0

        def extractSubGrid(srcGrid, startX, startY, endX, endY):
            def extractRow(row, startCol, endCol):
                tempRow = []
                i = startCol
                while i <= endCol:
                    tempRow.append(row[i])
                    i += 1
                return tempRow

            result = []
            r = startX
            while r <= endX:
                result.append(extractRow(srcGrid[r], startY, endY))
                r += 1
            return result

        startRow = 0
        while startRow < height:
            startCol = 0
            while startCol < width:
                endRow = startRow
                while endRow < height:
                    endCol = startCol
                    while endCol < width:
                        candidateSubmatrix = extractSubGrid(grid, startRow, startCol, endRow, endCol)

                        exceedsLimitFlag = anyElementExceedsLimit(candidateSubmatrix)
                        orderViolationFlag = hasViolationInOrder(candidateSubmatrix)

                        if not exceedsLimitFlag and not orderViolationFlag:
                            totalMatches += 1

                        endCol += 1
                    endRow += 1
                startCol += 1
            startRow += 1

        return totalMatches