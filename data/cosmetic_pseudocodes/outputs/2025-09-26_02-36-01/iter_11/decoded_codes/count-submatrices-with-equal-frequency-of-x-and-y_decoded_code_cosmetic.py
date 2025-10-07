class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        alpha = len(grid)
        beta = len(grid[0])

        # prefix_data[a][b] = [count_X_up_to_a_b, count_Y_up_to_a_b]
        prefix_data = [[[0, 0] for _ in range(beta + 1)] for __ in range(alpha + 1)]

        def compute_prefix(a, b):
            first_val = prefix_data[a - 1][b][0] + prefix_data[a][b - 1][0] - prefix_data[a - 1][b - 1][0]
            second_val = prefix_data[a - 1][b][1] + prefix_data[a][b - 1][1] - prefix_data[a - 1][b - 1][1]

            if grid[a - 1][b - 1] == 'X':
                first_val += 1
            elif grid[a - 1][b - 1] == 'Y':
                second_val += 1

            prefix_data[a][b][0] = first_val
            prefix_data[a][b][1] = second_val

        def iterate_rows_col(current_row):
            if current_row > alpha:
                return

            def iterate_cols(current_col):
                if current_col > beta:
                    return

                compute_prefix(current_row, current_col)
                iterate_cols(current_col + 1)

            iterate_cols(1)
            iterate_rows_col(current_row + 1)

        iterate_rows_col(1)

        tally = 0

        def count_loop(ridx):
            nonlocal tally
            if ridx > alpha:
                return

            def count_inner(cidx):
                nonlocal tally
                if cidx > beta:
                    return

                count_x = prefix_data[ridx][cidx][0]
                count_y = prefix_data[ridx][cidx][1]

                if count_x > 0 and count_x == count_y:
                    tally += 1

                count_inner(cidx + 1)

            count_inner(1)
            count_loop(ridx + 1)

        count_loop(1)

        return tally