class Solution:
    def countSubmatrices(self, grid, k):
        rowsCount = len(grid)
        colsCount = len(grid[0])
        totalCount = 0

        def is_valid_submatrix(submat):
            for row in submat:
                for val in row:
                    if val > k:
                        return False
            return True

        def is_sorted_submatrix(submat):
            for row in submat:
                for c in range(1, len(row)):
                    if not (row[c] <= row[c - 1]):
                        return False
            return True

        for startRow in range(rowsCount):
            for startCol in range(colsCount):
                for endRow in range(startRow, rowsCount):
                    for endCol in range(startCol, colsCount):
                        tempSubmatrix = [grid[r][startCol:endCol + 1] for r in range(startRow, endRow + 1)]
                        if is_valid_submatrix(tempSubmatrix) and is_sorted_submatrix(tempSubmatrix):
                            totalCount += 1

        return totalCount