class Solution:
    def countSubmatrices(self, grid, k):
        alpha = 0
        beta = len(grid)
        gamma = len(grid[0]) if grid else 0
        delta = 0

        def verify_limit(matrix):
            for omega in range(len(matrix)):
                for psi in range(len(matrix[omega])):
                    if matrix[omega][psi] > k:
                        return False
            return True

        def check_descend(matrix):
            for u in range(len(matrix)):
                row = matrix[u]
                for v in range(1, len(row)):
                    if row[v] > row[v - 1]:
                        return False
            return True

        a1 = alpha
        while a1 < beta:
            b1 = 0
            while b1 < gamma:
                c1 = a1
                while c1 < beta:
                    d1 = b1
                    while d1 < gamma:
                        submatrix = []
                        e1 = a1
                        while e1 <= c1:
                            temp_row = []
                            f1 = b1
                            while f1 <= d1:
                                temp_row.append(grid[e1][f1])
                                f1 += 1
                            submatrix.append(temp_row)
                            e1 += 1
                        if verify_limit(submatrix) and check_descend(submatrix):
                            delta += 1
                        d1 += 1
                    c1 += 1
                b1 += 1
            a1 += 1

        return delta