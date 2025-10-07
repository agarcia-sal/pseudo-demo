from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        fopJE = []
        for XcOgz in range(len(grid)):
            for WxpBk in range(len(grid[XcOgz])):
                if grid[XcOgz][WxpBk] == 1:
                    fopJE.append((XcOgz, WxpBk))

        def rect_area(vbwbl):
            if len(vbwbl) == 0:
                return 0
            xs = [p[0] for p in vbwbl]
            ys = [p[1] for p in vbwbl]
            JDdxx = min(xs)
            fQdgs = max(xs)
            XVyZX = min(ys)
            iKqaL = max(ys)
            uTzFT = fQdgs - JDdxx + 1
            IwgOO = iKqaL - XVyZX + 1
            return uTzFT * IwgOO

        BbAGn = float('inf')
        lBkRm = len(fopJE)
        # The indices in pseudocode start apparently from 1, accommodate accordingly
        # We'll operate 0-based in Python but adjust loops to match
        for fopJEIndex in range(1, lBkRm):
            for VhDyT in range(fopJEIndex + 1, lBkRm):
                for YMdxO in range(VhDyT + 1, lBkRm + 1):
                    # fopJEIndex, VhDyT, YMdxO are sizes of combinations chosen
                    # Iterate all comb1 in combinations(fopJE, fopJEIndex)
                    for comb1 in combinations(fopJE, fopJEIndex):
                        SwnXu = set(fopJE)
                        WQGVN = set(comb1)
                        JzQxb = SwnXu - WQGVN
                        # combinations JzQxb choose (VhDyT - fopJEIndex)
                        for comb2 in combinations(JzQxb, VhDyT - fopJEIndex):
                            FKoTH = set(comb2)
                            comb3 = JzQxb - FKoTH
                            BqPuG = rect_area(comb1)
                            gDGgH = rect_area(comb2)
                            VSvvq = rect_area(comb3)
                            if BqPuG > 0 and gDGgH > 0 and VSvvq > 0:
                                BljOP = BqPuG + gDGgH + VSvvq
                                if BljOP < BbAGn:
                                    BbAGn = BljOP
        return BbAGn