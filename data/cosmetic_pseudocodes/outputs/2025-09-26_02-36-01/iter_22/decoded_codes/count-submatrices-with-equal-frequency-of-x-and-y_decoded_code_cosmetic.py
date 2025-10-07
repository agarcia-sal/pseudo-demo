class Solution:
    def numberOfSubmatrices(self, grid):
        if not grid or not grid[0]:
            return 0

        alpha = len(grid)
        beta = len(grid[0])

        gamma = alpha + 1
        delta = beta + 1

        # Initialize prefix_sum as a 3D list: gamma x delta x 2, filled with zeros
        prefix_sum = [[[0, 0] for _ in range(delta)] for _ in range(gamma)]

        k = 1
        while k <= alpha:
            m = 1
            while m <= beta:
                prefix_sum[k][m][0] = (
                    prefix_sum[k - 1][m][0] + prefix_sum[k][m - 1][0] - prefix_sum[k - 1][m - 1][0]
                )
                prefix_sum[k][m][1] = (
                    prefix_sum[k - 1][m][1] + prefix_sum[k][m - 1][1] - prefix_sum[k - 1][m - 1][1]
                )

                if grid[k - 1][m - 1] == 'X':
                    prefix_sum[k][m][0] += 1
                elif grid[k - 1][m - 1] == 'Y':
                    prefix_sum[k][m][1] += 1

                m += 1
            k += 1

        total = 0
        for a in range(1, alpha + 1):
            b = 1
            while b <= beta:
                xq = prefix_sum[a][b][0]
                yq = prefix_sum[a][b][1]
                if xq > 0 and xq == yq:
                    total += 1
                b += 1

        return total