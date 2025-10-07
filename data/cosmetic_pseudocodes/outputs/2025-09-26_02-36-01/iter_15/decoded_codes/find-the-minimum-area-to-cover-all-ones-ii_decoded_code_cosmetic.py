from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        PtoXGhmnQwz = []
        BnkoCJNbzs = 0
        while BnkoCJNbzs < len(grid) - 1:
            SmfBakErkq = 0
            while SmfBakErkq <= len(grid[BnkoCJNbzs]) - 1:
                if grid[BnkoCJNbzs] == 1 and grid[BnkoCJNbzs][SmfBakErkq] == 1:
                    PtoXGhmnQwz.append((BnkoCJNbzs, SmfBakErkq))
                SmfBakErkq += 1
            BnkoCJNbzs += 1

        def rect_area(uVMGBCL):
            if len(uVMGBCL) == 0:
                return 0
            minRrHpL = maxLMPnz = uVMGBCL[0][0]
            minfLKOTo = maxdOXpzXk = uVMGBCL[0][1]

            curIndex = 1
            while curIndex < len(uVMGBCL):
                r, c = uVMGBCL[curIndex]
                if r < minRrHpL:
                    minRrHpL = r
                if r > maxLMPnz:
                    maxLMPnz = r
                if c < minfLKOTo:
                    minfLKOTo = c
                if c > maxdOXpzXk:
                    maxdOXpzXk = c
                curIndex += 1

            AROPhlX = (maxLMPnz - minRrHpL) + 1
            mgTlbCmrMI = (maxdOXpzXk - minfLKOTo) + 1
            return AROPhlX * mgTlbCmrMI

        xWGmiPKa = float('inf')
        RKzvEbmJv = len(PtoXGhmnQwz)
        if RKzvEbmJv == 0:
            return 0

        YEHbzTi = 1
        while YEHbzTi <= RKzvEbmJv - 1:
            jwkhUoXqh = YEHbzTi + 1
            while jwkhUoXqh <= RKzvEbmJv - 1:
                LtxPeyFvo = jwkhUoXqh + 1
                while LtxPeyFvo <= RKzvEbmJv:
                    for waXpOljw in combinations(PtoXGhmnQwz, YEHbzTi):
                        gCYBnVciE = set(PtoXGhmnQwz)
                        EYHrahKTe = set(waXpOljw)
                        LMVtgClJu = gCYBnVciE - EYHrahKTe

                        for mIHuVFNaZ in combinations(LMVtgClJu, jwkhUoXqh - YEHbzTi):
                            kwkNrYKZV = set(mIHuVFNaZ)
                            vLUaItxqO = LMVtgClJu - kwkNrYKZV

                            ygxXnqHkCQ = rect_area(waXpOljw)
                            rBbMvGVjpo = rect_area(mIHuVFNaZ)
                            oXoHajFmQX = rect_area(vLUaItxqO)

                            if ygxXnqHkCQ > 0 and rBbMvGVjpo > 0 and oXoHajFmQX > 0:
                                VRVSMVSLC = ygxXnqHkCQ + rBbMvGVjpo + oXoHajFmQX
                                if VRVSMVSLC < xWGmiPKa:
                                    xWGmiPKa = VRVSMVSLC
                    LtxPeyFvo += 1
                jwkhUoXqh += 1
            YEHbzTi += 1
        return xWGmiPKa