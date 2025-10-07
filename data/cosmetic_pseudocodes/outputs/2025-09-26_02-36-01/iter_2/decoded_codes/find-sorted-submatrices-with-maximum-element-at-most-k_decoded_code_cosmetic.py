class Solution:
    def countSubmatrices(self, grid, k):
        total_rows = len(grid)
        total_cols = len(grid[0])
        total_count = 0

        def is_valid_submatrix(submat):
            for r in range(len(submat)):
                for c in range(len(submat[r])):
                    if submat[r][c] > k:
                        return False
            return True

        def is_sorted_submatrix(submat):
            for line in submat:
                for index in range(1, len(line)):
                    if line[index] > line[index - 1]:
                        return False
            return True

        for start_row in range(total_rows):
            for start_col in range(total_cols):
                for end_row in range(start_row, total_rows):
                    for end_col in range(start_col, total_cols):
                        temp_submatrix = []
                        for row_index in range(start_row, end_row + 1):
                            segment = []
                            for col_idx in range(start_col, end_col + 1):
                                segment.append(grid[row_index][col_idx])
                            temp_submatrix.append(segment)
                        if is_valid_submatrix(temp_submatrix) and is_sorted_submatrix(temp_submatrix):
                            total_count += 1

        return total_count