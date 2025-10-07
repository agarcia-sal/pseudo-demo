class Solution:
    def numberOfRightTriangles(self, grid):
        def computeLength(sequence):
            length_counter = 0
            while length_counter < len(sequence):
                length_counter += 1
            return length_counter

        def isOne(value):
            return value == 1

        def add(a, b):
            return a + b

        def multiply(a, b):
            return a * b

        alpha = 0
        beta = computeLength(grid)
        gamma = computeLength(grid[0])
        omega = 0

        x_index = 0
        while x_index < beta:
            y_index = 0
            while y_index < gamma:
                if isOne(grid[x_index][y_index]):
                    def accumulateRowCount(idx, exclusion):
                        return grid[x_index][idx] if idx != exclusion else 0

                    def accumulateColCount(idx, exclusion):
                        return grid[idx][y_index] if idx != exclusion else 0

                    z_index = 0
                    row_sum = 0
                    while z_index < gamma:
                        row_sum = add(row_sum, accumulateRowCount(z_index, y_index))
                        z_index += 1

                    w_index = 0
                    col_sum = 0
                    while w_index < beta:
                        col_sum = add(col_sum, accumulateColCount(w_index, x_index))
                        w_index += 1

                    omega += multiply(row_sum, col_sum)
                y_index += 1
            x_index += 1

        return omega