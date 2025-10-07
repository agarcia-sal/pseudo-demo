class Solution:
    def numberOfRightTriangles(self, grid):
        alpha = 0
        beta = len(grid)
        gamma = len(grid[0]) if beta > 0 else 0
        delta = 0

        epsilon = 0
        while epsilon < beta:
            zeta = 0
            while zeta < gamma:
                if grid[epsilon][zeta] == 1:
                    eta = 0
                    iota = 0
                    while iota < gamma:
                        if iota != zeta:
                            eta += grid[epsilon][iota]
                        iota += 1
                    kappa = 0
                    mu = 0
                    while mu < beta:
                        if mu != epsilon:
                            kappa += grid[mu][zeta]
                        mu += 1
                    delta += eta * kappa
                zeta += 1
            epsilon += 1

        return delta