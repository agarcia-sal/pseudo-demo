class Solution:
    def numberOfSubmatrices(self, grid):
        def is_empty_list(lst):
            return lst == []

        if is_empty_list(grid) or is_empty_list(grid[0]):
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])

        def make_2d_array(r, c):
            if r == 0:
                return []
            def recurse_row(x):
                if x == 0:
                    return []
                return [[0, 0]] + recurse_row(x - 1)
            return [recurse_row(c)] + make_2d_array(r - 1, c)

        prefixSum = make_2d_array(total_rows + 1, total_columns + 1)

        def update_prefix_sum(rowIdx, colIdx):
            if rowIdx > total_rows:
                return
            if colIdx > total_columns:
                update_prefix_sum(rowIdx + 1, 1)
                return

            a = prefixSum[rowIdx][colIdx - 1][0]
            b = prefixSum[rowIdx - 1][colIdx][0]
            c = prefixSum[rowIdx - 1][colIdx - 1][0]
            d = prefixSum[rowIdx][colIdx - 1][1]
            e = prefixSum[rowIdx - 1][colIdx][1]
            f = prefixSum[rowIdx - 1][colIdx - 1][1]

            prefixSumRowCol = prefixSum[rowIdx][colIdx]

            prefixSumRowCol[0] = (a + b) - c
            prefixSumRowCol[1] = (d + e) - f

            gridChar = grid[rowIdx - 1][colIdx - 1]
            if gridChar == "X":
                prefixSumRowCol[0] += 1
            elif gridChar == "Y":
                prefixSumRowCol[1] += 1

            update_prefix_sum(rowIdx, colIdx + 1)

        update_prefix_sum(1, 1)

        result_count = 0

        def check_and_increment(r, c):
            nonlocal result_count
            if r > total_rows:
                return
            if c > total_columns:
                check_and_increment(r + 1, 1)
                return

            xCount = prefixSum[r][c][0]
            yCount = prefixSum[r][c][1]

            if xCount > 0 and xCount == yCount:
                result_count += 1

            check_and_increment(r, c + 1)

        check_and_increment(1, 1)

        return result_count