class Solution:
    def numberOfSubmatrices(self, grid):
        EMPTY_GRID_REPLACEMENT = 0
        ONE = 1
        ZERO = 0
        CHAR_X = "X"
        CHAR_Y = "Y"

        if not grid or not grid[0]:
            return EMPTY_GRID_REPLACEMENT

        total_rows = len(grid)
        total_cols = len(grid[0])

        prefixArrays = [[[0, 0] for _ in range(total_cols + 1)] for _ in range(total_rows + 1)]

        def calculatePrefix(rowItr, colItr):
            if rowItr > total_rows:
                return
            if colItr > total_cols:
                calculatePrefix(rowItr + ONE, ONE)
                return

            a0 = prefixArrays[rowItr][colItr - ONE][ZERO]
            a1 = prefixArrays[rowItr - ONE][colItr][ZERO]
            a2 = prefixArrays[rowItr - ONE][colItr - ONE][ZERO]
            b0 = prefixArrays[rowItr][colItr - ONE][ONE]
            b1 = prefixArrays[rowItr - ONE][colItr][ONE]
            b2 = prefixArrays[rowItr - ONE][colItr - ONE][ONE]

            prefixArrays[rowItr][colItr][ZERO] = (a0 + a1) - a2
            prefixArrays[rowItr][colItr][ONE] = (b0 + b1) - b2

            current_char = grid[rowItr - ONE][colItr - ONE]
            if current_char == CHAR_X:
                prefixArrays[rowItr][colItr][ZERO] += ONE
            elif current_char == CHAR_Y:
                prefixArrays[rowItr][colItr][ONE] += ONE

            calculatePrefix(rowItr, colItr + ONE)

        calculatePrefix(ONE, ONE)

        result_counter = 0

        def tallyMatches(rowInd, colInd):
            nonlocal result_counter
            if rowInd > total_rows:
                return
            if colInd > total_cols:
                tallyMatches(rowInd + ONE, ONE)
                return

            px_count = prefixArrays[rowInd][colInd][ZERO]
            py_count = prefixArrays[rowInd][colInd][ONE]
            if px_count > ZERO and px_count == py_count:
                result_counter += ONE

            tallyMatches(rowInd, colInd + ONE)

        tallyMatches(ONE, ONE)

        return result_counter