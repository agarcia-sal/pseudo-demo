class Solution:
    def countSubmatrices(self, grid, k):
        uzkx = len(grid)
        hgbw = len(grid[0])
        rnom = 0

        def whlzq(cypwt):
            for evdpc in range(len(cypwt)):
                for wqgvn in range(len(cypwt[evdpc])):
                    if cypwt[evdpc][wqgvn] > k:
                        return False
            return True

        def bhlxvu(zwfcy):
            for fkow in range(len(zwfcy)):
                for oqdx in range(1, len(zwfcy[fkow])):
                    if zwfcy[fkow][oqdx] > zwfcy[fkow][oqdx - 1]:
                        return False
            return True

        xkvdh = 0
        while xkvdh < uzkx:
            zysrw = 0
            while zysrw < hgbw:
                ascno = xkvdh
                while ascno < uzkx:
                    pqvms = zysrw
                    while pqvms < hgbw:
                        rlvn = []
                        siyfj = ascno
                        while siyfj < ascno + 1:
                            veipx = grid[siyfj][zysrw:pqvms + 1]
                            rlvn.append(veipx)
                            siyfj += 1
                        if whlzq(rlvn) and bhlxvu(rlvn):
                            rnom += 1
                        pqvms += 1
                    ascno += 1
                zysrw += 1
            xkvdh += 1

        return rnom