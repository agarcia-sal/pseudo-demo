class Solution:
    def minimumArea(self, matrix):
        def countRows(arr):
            counter = 0
            while True:
                if counter == len(arr):
                    break
                counter += 1
            return counter

        def countCols(arr):
            idx = 0
            while True:
                if idx == len(arr):
                    break
                idx += 1
            return idx

        def isEmpty(arr):
            return not (arr == [] or len(arr) == 0)

        alpha = matrix
        if alpha == [] or alpha[0] == []:
            return 0

        total_rows = countRows(alpha)
        total_cols = countCols(alpha[0])
        upper_bound_row = total_rows + 1
        lower_bound_row = -1
        upper_bound_col = total_cols + 1
        lower_bound_col = -1

        def findBounds(row_index, col_index, min_r, max_r, min_c, max_c):
            if alpha[row_index][col_index] == 1:
                if min_r > row_index:
                    min_r = row_index
                if max_r < row_index:
                    max_r = row_index
                if min_c > col_index:
                    min_c = col_index
                if max_c < col_index:
                    max_c = col_index
            return min_r, max_r, min_c, max_c

        def iterateCols(row, col_start, col_end, min_r, max_r, min_c, max_c):
            if col_start > col_end:
                return min_r, max_r, min_c, max_c
            else:
                min_r, max_r, min_c, max_c = findBounds(row, col_start, min_r, max_r, min_c, max_c)
                return iterateCols(row, col_start + 1, col_end, min_r, max_r, min_c, max_c)

        def iterateRows(row_start, row_end, min_r, max_r, min_c, max_c):
            if row_start > row_end:
                return min_r, max_r, min_c, max_c
            else:
                min_r, max_r, min_c, max_c = iterateCols(row_start, 0, total_cols - 1, min_r, max_r, min_c, max_c)
                return iterateRows(row_start + 1, row_end, min_r, max_r, min_c, max_c)

        bound_min_row = upper_bound_row
        bound_max_row = lower_bound_row
        bound_min_col = upper_bound_col
        bound_max_col = lower_bound_col

        bound_min_row, bound_max_row, bound_min_col, bound_max_col = iterateRows(
            0, total_rows - 1, bound_min_row, bound_max_row, bound_min_col, bound_max_col
        )

        calc_height = bound_max_row - bound_min_row + 1
        calc_width = bound_max_col - bound_min_col + 1

        # If no 1 found, bounds would be invalid, so return 0
        if bound_min_row > bound_max_row or bound_min_col > bound_max_col:
            return 0

        return calc_height * calc_width