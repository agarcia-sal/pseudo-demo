class Solution:
    def countSubmatrices(self, grid, k):
        alpha = len(grid)
        beta = len(grid[0])
        omega = 0

        def check_all_elements(matrix):
            for row in matrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def verify_non_increasing(matrix):
            for row in matrix:
                for i in range(1, len(row)):
                    if row[i] > row[i-1]:
                        return False
            return True

        for firstRow in range(alpha):
            for firstCol in range(beta):
                for lastRow in range(firstRow, alpha):
                    for lastCol in range(firstCol, beta):
                        temp_matrix = []
                        for idx_row in range(firstRow, lastRow + 1):
                            segment = grid[idx_row][firstCol:lastCol + 1]
                            temp_matrix.append(segment)
                        if check_all_elements(temp_matrix) and verify_non_increasing(temp_matrix):
                            omega += 1

        return omega