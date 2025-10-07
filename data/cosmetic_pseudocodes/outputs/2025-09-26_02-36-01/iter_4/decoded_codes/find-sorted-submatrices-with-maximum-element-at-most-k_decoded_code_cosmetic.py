class Solution:
    def countSubmatrices(self, grid, k):
        rowsCount = len(grid)
        colsCount = len(grid[0]) if rowsCount > 0 else 0
        totalSubmatrices = 0

        def is_valid_submatrix(submat):
            for row in submat:
                for val in row:
                    if val > k:
                        return False
            return True

        def is_sorted_submatrix(submat):
            for row in submat:
                for c in range(1, len(row)):
                    if row[c] > row[c - 1]:
                        return False
            return True

        for startX in range(rowsCount):
            for startY in range(colsCount):
                for endX in range(startX, rowsCount):
                    for endY in range(startY, colsCount):
                        tempSubmatrix = []
                        for rowI in range(startX, endX + 1):
                            rowSlice = grid[rowI][startY : endY + 1]
                            tempSubmatrix.append(rowSlice)
                        if is_valid_submatrix(tempSubmatrix) and is_sorted_submatrix(tempSubmatrix):
                            totalSubmatrices += 1

        return totalSubmatrices