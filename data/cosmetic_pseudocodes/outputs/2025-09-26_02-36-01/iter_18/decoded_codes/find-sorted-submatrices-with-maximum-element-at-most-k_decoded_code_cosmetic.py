class Solution:
    def countSubmatrices(self, grid, k):
        q = len(grid)
        r = len(grid[0]) if q > 0 else 0
        z = 0

        def qwt(mxv):
            for row in mxv:
                for val in row:
                    if val > k:
                        return False
            return True

        def jpk(sdm):
            for row in sdm:
                for i in range(1, len(row)):
                    if row[i] > row[i - 1]:
                        return False
            return True

        xfl = 0
        while xfl < q:
            syf = 0
            while syf < r:
                mof = xfl
                while mof < q:
                    uht = syf
                    while uht < r:
                        subm = []
                        xbq = mof
                        while xbq >= xfl:
                            fkx = grid[xbq]
                            row_slice = fkx[syf:uht + 1]
                            subm.append(row_slice)
                            xbq -= 1
                        if qwt(subm) and jpk(subm):
                            z += 1
                        uht += 1
                    mof += 1
                syf += 1
            xfl += 1

        return z