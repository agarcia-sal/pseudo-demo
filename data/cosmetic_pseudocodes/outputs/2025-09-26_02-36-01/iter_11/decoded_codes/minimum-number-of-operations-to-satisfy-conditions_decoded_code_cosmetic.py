class Solution:
    def minimumOperations(self, grid):
        beta = len(grid)
        omega = len(grid[0])
        delta = 0

        def check_and_update(x, y):
            nonlocal delta
            if grid[x][y] != grid[x + 1][y]:
                delta += 1
                grid[x + 1][y] = grid[x][y]

        def assign_different_value(x, y):
            nonlocal delta
            for alpha in range(10):
                if alpha != grid[x][y]:
                    grid[x][y + 1] = alpha
                    break
            delta += 1

        kappa = 0
        while kappa < omega:
            lambda_ = 0
            while lambda_ < beta - 1:
                check_and_update(lambda_, kappa)
                lambda_ += 1

            mu = 0
            while mu < beta:
                if (kappa < omega - 1) and (grid[mu][kappa] == grid[mu][kappa + 1]):
                    assign_different_value(mu, kappa)
                mu += 1

            kappa += 1

        return delta