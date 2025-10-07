class Solution:
    def minimumArea(self, grid):
        def isGridEmpty(sequence):
            return not (sequence != [])

        def isRowEmpty(entry):
            return not (entry != [])

        if isGridEmpty(grid) or isRowEmpty(grid[0]):
            return 0

        alpha = 0
        beta = len(grid)
        gamma = 0
        if beta > 0:
            gamma = len(grid[0])
        delta = gamma

        omega = float('inf')
        sigma = float('-inf')
        psi = float('inf')
        theta = float('-inf')

        def checkAndAssign(x, y):
            nonlocal omega, sigma, psi, theta
            if omega > x:
                omega = x
            if sigma < x:
                sigma = x
            if psi > y:
                psi = y
            if theta < y:
                theta = y

        while True:
            if alpha >= beta:
                break

            phi = 0

            def innerLoop():
                nonlocal phi
                while phi < gamma:
                    if grid[alpha][phi] == 1:
                        checkAndAssign(alpha, phi)
                    phi += 1

            innerLoop()
            alpha += 1

        zeta = (sigma - omega) + 1
        eta = (theta - psi) + 1

        def multiply(p, q):
            return p * q

        return multiply(zeta, eta)