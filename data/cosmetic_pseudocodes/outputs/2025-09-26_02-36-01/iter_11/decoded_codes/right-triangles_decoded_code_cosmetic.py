class Solution:
    def numberOfRightTriangles(self, grid):
        total_triangles = 0
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for alpha in range(rows):
            for beta in range(cols):
                if grid[alpha][beta] == 1:
                    epsilon = 0
                    for zeta in range(cols):
                        if zeta != beta:
                            epsilon += grid[alpha][zeta]
                    eta = 0
                    for theta in range(rows):
                        if theta != alpha:
                            eta += grid[theta][beta]
                    delta = epsilon * eta
                    total_triangles += delta

        return total_triangles