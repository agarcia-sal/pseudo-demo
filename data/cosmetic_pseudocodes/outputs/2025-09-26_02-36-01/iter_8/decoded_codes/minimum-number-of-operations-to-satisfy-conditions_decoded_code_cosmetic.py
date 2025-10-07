class Solution:
    def minimumOperations(self, grid):
        alpha = len(grid)
        beta = len(grid[0])
        gamma = 0

        delta = 0
        while delta <= beta - 2:
            zeta = 0
            while zeta <= alpha - 2:
                if grid[zeta][delta] != grid[zeta + 1][delta]:
                    gamma += 1
                    grid[zeta + 1][delta] = grid[zeta][delta]
                zeta += 1

            epsilon = 0
            while epsilon < alpha:
                if delta < beta - 2 and grid[epsilon][delta] == grid[epsilon][delta + 1]:
                    gamma += 1
                    kappa = 0
                    while kappa <= 10:
                        if kappa != grid[epsilon][delta]:
                            grid[epsilon][delta + 1] = kappa
                            break
                        kappa += 1
                epsilon += 1
            delta += 1

        return gamma