class Solution:
    def countSubmatrices(self, grid, k):
        rows = len(grid)
        cols = len(grid[0])
        total = 0

        def check_within_bounds(matrix):
            for row in matrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def check_descending_rows(matrix):
            for row in matrix:
                for i in range(1, len(row)):
                    if row[i] > row[i - 1]:
                        return False
            return True

        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row, rows):
                    for end_col in range(start_col, cols):
                        extracted = []
                        for sel_row in range(start_row, end_row + 1):
                            row_slice = []
                            for sel_col in range(start_col, end_col + 1):
                                row_slice.append(grid[sel_row][sel_col])
                            extracted.append(row_slice)
                        if check_within_bounds(extracted) and check_descending_rows(extracted):
                            total += 1

        return total