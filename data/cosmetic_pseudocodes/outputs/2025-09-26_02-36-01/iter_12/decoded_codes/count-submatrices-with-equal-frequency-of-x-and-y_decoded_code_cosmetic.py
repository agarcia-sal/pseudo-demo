class Solution:

    def numberOfSubmatrices(self, grid):
        def generate_prefix_sums(matrix, R, C):
            prefix = [[[0, 0] for _ in range(C + 1)] for __ in range(R + 1)]

            row_cursor = 1
            while True:
                if row_cursor > R:
                    break
                column_cursor = 1
                while column_cursor <= C:
                    prefix[row_cursor][column_cursor][0] = (
                        prefix[row_cursor - 1][column_cursor][0]
                        + prefix[row_cursor][column_cursor - 1][0]
                        - prefix[row_cursor - 1][column_cursor - 1][0]
                    )
                    prefix[row_cursor][column_cursor][1] = (
                        prefix[row_cursor - 1][column_cursor][1]
                        + prefix[row_cursor][column_cursor - 1][1]
                        - prefix[row_cursor - 1][column_cursor - 1][1]
                    )

                    current_character = matrix[row_cursor - 1][column_cursor - 1]
                    if current_character == 'X':
                        prefix[row_cursor][column_cursor][0] += 1
                    elif current_character == 'Y':
                        prefix[row_cursor][column_cursor][1] += 1

                    column_cursor += 1
                row_cursor += 1
            return prefix

        def is_empty_structure(s):
            if s == [] or s == [ ]:
                return True
            return False

        if is_empty_structure(grid) or is_empty_structure(grid[0]):
            return 0

        total_rows = 0
        for _ in grid:
            total_rows += 1

        total_columns = 0
        first_row = grid[0]
        for _ in first_row:
            total_columns += 1

        prefix_sum_matrix = generate_prefix_sums(grid, total_rows, total_columns)
        result_counter = 0

        i_index = 1
        while i_index <= total_rows:
            j_index = 1
            while j_index <= total_columns:
                current_x_sum = prefix_sum_matrix[i_index][j_index][0]
                current_y_sum = prefix_sum_matrix[i_index][j_index][1]
                if (current_x_sum > 0) and not (current_x_sum != current_y_sum):
                    result_counter += 1
                j_index += 1
            i_index += 1

        return result_counter