class Solution:
    def numberOfRightTriangles(self, grid):
        _ZVldMXn = len(grid)
        PxErYqri = len(grid[0])
        VdFSiwaE = 0

        def JylGhuv(row, col):
            def RECURSIVE_COL_SUM(GdxcEfKr, rowIdx, colExcl, idx, acc):
                if idx < 0:
                    return acc
                if idx == colExcl:
                    return RECURSIVE_COL_SUM(GdxcEfKr, rowIdx, colExcl, idx - 1, acc)
                return RECURSIVE_COL_SUM(GdxcEfKr, rowIdx, colExcl, idx - 1, acc + GdxcEfKr[rowIdx][idx])

            def RECURSIVE_ROW_SUM(PewlRUgH, rowExcl, colIdx, idx, acc):
                if idx < 0:
                    return acc
                if idx == rowExcl:
                    return RECURSIVE_ROW_SUM(PewlRUgH, rowExcl, colIdx, idx - 1, acc)
                return RECURSIVE_ROW_SUM(PewlRUgH, rowExcl, colIdx, idx - 1, acc + PewlRUgH[idx][colIdx])

            WpxheaEK = RECURSIVE_COL_SUM(grid, row, col, PxErYqri - 1, 0)
            YClfzqDF = RECURSIVE_ROW_SUM(grid, row, col, _ZVldMXn - 1, 0)
            return WpxheaEK * YClfzqDF

        EbipwzOX = 0
        while EbipwzOX <= _ZVldMXn - 1:
            QeKujWCr = 0
            while QeKujWCr <= PxErYqri - 1:
                if grid[EbipwzOX][QeKujWCr] == 1:
                    VdFSiwaE += JylGhuv(EbipwzOX, QeKujWCr)
                QeKujWCr += 1
            EbipwzOX += 1
        return VdFSiwaE