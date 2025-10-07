class Solution:
    def countSubmatrices(self, grid, k):
        if not grid or not grid[0]:
            return 0

        rowCount = len(grid)
        colCount = len(grid[0])

        cumulative_matrix = [[0] * colCount for _ in range(rowCount)]

        total_submatrices = 0

        for p in range(rowCount):
            for q in range(colCount):
                if p == 0 and q == 0:
                    cumulative_matrix[p][q] = grid[p][q]
                elif p == 0:
                    cumulative_matrix[p][q] = cumulative_matrix[p][q - 1] + grid[p][q]
                elif q == 0:
                    cumulative_matrix[p][q] = cumulative_matrix[p - 1][q] + grid[p][q]
                else:
                    top_left_val = cumulative_matrix[p - 1][q - 1]
                    top_val = cumulative_matrix[p - 1][q]
                    left_val = cumulative_matrix[p][q - 1]
                    current_val = grid[p][q]
                    cumulative_matrix[p][q] = top_val + left_val - top_left_val + current_val

                if cumulative_matrix[p][q] <= k:
                    total_submatrices += 1

        return total_submatrices