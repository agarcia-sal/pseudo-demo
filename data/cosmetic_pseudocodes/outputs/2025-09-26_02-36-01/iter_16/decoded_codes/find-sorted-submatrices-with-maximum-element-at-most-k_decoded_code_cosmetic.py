class Solution:
    def countSubmatrices(self, grid, k):
        A = len(grid)
        B = len(grid[0])
        C = 0

        def is_valid_submatrix(submatrix):
            for row in submatrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def is_sorted_submatrix(submatrix):
            for row in submatrix:
                for i in range(1, len(row)):
                    if row[i] > row[i - 1]:
                        return False
            return True

        for H in range(A):
            for I in range(B):
                for J in range(H, A):
                    for K_ in range(I, B):
                        M = []
                        # Construct submatrix rows from J to J (single row as per original)
                        for N in range(J, J + 1):
                            # Slice from I to K_ inclusive
                            P = grid[N][I:K_ + 1]
                            M.append(P)
                        if is_valid_submatrix(M) and is_sorted_submatrix(M):
                            C += 1

        return C