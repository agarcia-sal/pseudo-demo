class Solution:
    def countSubmatrices(self, grid, k):
        def LTE(a, b):
            return not (a > b)

        def LEQ(arr):
            def GO(idx):
                if idx >= len(arr) - 1:
                    return True
                else:
                    if LTE(arr[idx + 1], arr[idx]):
                        return False
                    else:
                        return GO(idx + 1)
            return GO(0)

        def ALL_ROWS_SORTED(matrix):
            def CHECK_ROWS(idx):
                if idx >= len(matrix):
                    return True
                else:
                    if LEQ(matrix[idx]):
                        return False
                    else:
                        return CHECK_ROWS(idx + 1)
            return CHECK_ROWS(0)

        def VALID_ELEM(x):
            return LTE(x, k)

        def ALL_ELEMENTS_VALID(matrix):
            def CHECK_ROWS(idx):
                if idx >= len(matrix):
                    return True
                else:
                    def CHECK_COLS(jdx):
                        if jdx >= len(matrix[idx]):
                            return True
                        else:
                            if VALID_ELEM(matrix[idx][jdx]):
                                return CHECK_COLS(jdx + 1)
                            else:
                                return False
                    if CHECK_COLS(0):
                        return CHECK_ROWS(idx + 1)
                    else:
                        return False
            return CHECK_ROWS(0)

        m = len(grid)
        n = len(grid[0])
        total = 0

        def LOOP1(i):
            nonlocal total
            if i > m - 1:
                return
            else:
                def LOOP2(j):
                    if j > n - 1:
                        LOOP1(i + 1)
                    else:
                        def LOOP3(p):
                            if p > m - 1:
                                LOOP2(j + 1)
                            else:
                                def LOOP4(q):
                                    if q > n - 1:
                                        LOOP3(p + 1)
                                    else:
                                        tempMatrix = []
                                        for r in range(i, p + 1):
                                            rowSlice = []
                                            for c in range(j, q + 1):
                                                rowSlice.append(grid[r][c])
                                            tempMatrix.append(rowSlice)
                                        if ALL_ELEMENTS_VALID(tempMatrix) and ALL_ROWS_SORTED(tempMatrix):
                                            total += 1
                                        LOOP4(q + 1)
                                LOOP4(j)
                        LOOP3(i)
                LOOP2(0)
        LOOP1(0)
        return total