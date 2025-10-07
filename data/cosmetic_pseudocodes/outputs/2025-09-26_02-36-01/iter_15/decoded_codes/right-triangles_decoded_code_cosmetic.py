class Solution:
    def numberOfRightTriangles(self, grid):
        alpha = 0
        beta = len(grid)
        gamma = len(grid[0]) if beta > 0 else 0
        delta = 0

        def incrementIfNotEqual(x, y, count_ref, arr):
            if x != y:
                count_ref[0] += arr[x]

        def sumExceptIndexLine(line, excludeIdx):
            accumulator = [0]
            for iterator in range(len(line)):
                incrementIfNotEqual(iterator, excludeIdx, accumulator, line)
            return accumulator[0]

        def sumExceptIndexColumn(matrix, columnIdx, excludeRow):
            summation = 0
            for indexer in range(len(matrix)):
                if indexer == excludeRow:
                    continue
                summation += matrix[indexer][columnIdx]
            return summation

        while alpha < beta:
            epsilon = 0
            while epsilon < gamma:
                if grid[alpha][epsilon] != 0:
                    zeta = sumExceptIndexLine(grid[alpha], epsilon)
                    eta = sumExceptIndexColumn(grid, epsilon, alpha)
                    delta += zeta * eta
                epsilon += 1
            alpha += 1

        return delta