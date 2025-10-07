class Solution:
    def countSubmatrices(self, grid, k):
        Alpha = len(grid)
        Beta = len(grid[0]) if Alpha > 0 else 0
        Gamma = 0

        def validate_submatrix(matrix):
            # Returns False if any element in the matrix is greater than k
            for row in matrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def check_sorted_submatrix(matrix):
            # Checks if each row is sorted in non-increasing order (descending or equal)
            for row in matrix:
                for i in range(1, len(row)):
                    if row[i] > row[i - 1]:
                        return False
            return True

        for A in range(Alpha):
            for B in range(Beta):
                for C in range(A, Alpha):
                    for D in range(B, Beta):
                        submatrix = [row[B:D + 1] for row in grid[A:C + 1]]
                        if validate_submatrix(submatrix) and check_sorted_submatrix(submatrix):
                            Gamma += 1

        return Gamma