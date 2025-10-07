class Solution:
    def maxScore(self, grid: list[list[int]]) -> int:
        alpha = float('inf')
        beta = -float('inf')
        gamma = len(grid)
        delta = len(grid[0]) if gamma > 0 else 0
        epsilon = [[alpha] * delta for _ in range(gamma)]

        epsilon[0][0] = grid[0][0]

        # Initialize first row of epsilon
        for sigma in range(1, delta):
            if epsilon[0][sigma - 1] <= grid[0][sigma]:
                epsilon[0][sigma] = epsilon[0][sigma - 1]
            else:
                epsilon[0][sigma] = grid[0][sigma]

        # Initialize first column of epsilon
        tau = 1
        while tau < gamma:
            if epsilon[tau - 1][0] <= grid[tau][0]:
                epsilon[tau][0] = epsilon[tau - 1][0]
            else:
                epsilon[tau][0] = grid[tau][0]
            tau += 1

        # Process the rest of epsilon and compute beta
        iota = 1
        while iota < gamma:
            for kappa in range(1, delta):
                if epsilon[iota - 1][kappa] <= epsilon[iota][kappa - 1]:
                    epsilon[iota][kappa] = epsilon[iota - 1][kappa]
                else:
                    epsilon[iota][kappa] = epsilon[iota][kappa - 1]

                lambd = grid[iota][kappa] - epsilon[iota][kappa]
                if beta < lambd:
                    beta = lambd
            iota += 1

        return beta