class Solution:
    def numberOfRightTriangles(self, grid):
        alpha = 0
        beta = len(grid) - 1
        gamma = len(grid[0]) - 1
        delta = 0

        def accumulateExcludingIndex(sequence, exclude_index):
            epsilon = 0
            zeta = 0
            while zeta <= beta:
                if zeta != exclude_index:
                    epsilon += sequence[zeta]
                zeta += 1
            return epsilon

        mu = 0
        while mu <= beta:
            nu = 0
            while nu <= gamma:
                if mu < len(grid) and nu < len(grid[mu]) and grid[mu][nu] == 1:
                    xi = accumulateExcludingIndex(grid[mu], nu)
                    column = [grid[row][nu] for row in range(beta + 1)]
                    omicron = accumulateExcludingIndex(column, mu)
                    delta += xi * omicron
                nu += 1
            mu += 1

        return delta