class Solution:
    def minimumOperations(self, grid):
        alpha = 0
        beta = len(grid)
        gamma = len(grid[0])
        delta = 0

        for epsilon in range(gamma):
            for zeta in range(beta - 1):
                if grid[zeta][epsilon] != grid[zeta + 1][epsilon]:
                    delta += 1
                    grid[zeta + 1][epsilon] = grid[zeta][epsilon]

            eta = 0
            while eta <= beta - 1:
                if epsilon < gamma - 1 and grid[eta][epsilon] == grid[eta][epsilon + 1]:
                    delta += 1
                    theta = 0
                    while theta <= 9:
                        if theta != grid[eta][epsilon]:
                            grid[eta][epsilon + 1] = theta
                            break
                        theta += 1
                eta += 1

        return delta