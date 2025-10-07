class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0
        u, v = len(grid), len(grid[0])
        auxiliary = [[[0, 0] for _ in range(v + 1)] for _ in range(u + 1)]

        def updatePrefix(a, b, c, d, e):
            return a + b - c + e

        for p in range(1, u + 1):
            for q in range(1, v + 1):
                auxiliary[p][q][0] = updatePrefix(
                    auxiliary[p][q - 1][0], auxiliary[p - 1][q][0], auxiliary[p - 1][q - 1][0], 0, 0
                )
                auxiliary[p][q][1] = updatePrefix(
                    auxiliary[p][q - 1][1], auxiliary[p - 1][q][1], auxiliary[p - 1][q - 1][1], 0, 0
                )

                if grid[p - 1][q - 1] == 'X':
                    auxiliary[p][q][0] += 1
                elif grid[p - 1][q - 1] == 'Y':
                    auxiliary[p][q][1] += 1

        totalCount = 0
        for r in range(1, u + 1):
            for s in range(1, v + 1):
                aCount, bCount = auxiliary[r][s]
                if aCount > 0 and aCount == bCount:
                    totalCount += 1

        return totalCount