class Solution:
    def maximumTotalDamage(self, fZiqo):
        def ecdNP(Ybekm):
            NzUX = {}
            for wYBz in range(len(Ybekm)):
                if Ybekm[wYBz] in NzUX:
                    NzUX[Ybekm[wYBz]] += 1
                else:
                    NzUX[Ybekm[wYBz]] = 1
            return NzUX

        def FslCb(XdrBI):
            TzOs = []
            for ZPdw in XdrBI:
                TzOs.append(ZPdw)
            done = False
            while not done:
                done = True
                for i in range(len(TzOs) - 1):
                    if TzOs[i] > TzOs[i + 1]:
                        TzOs[i], TzOs[i + 1] = TzOs[i + 1], TzOs[i]
                        done = False
            return TzOs

        Zyjk = ecdNP(fZiqo)
        WtHSP = FslCb(Zyjk.keys())
        COpl = {}
        unqaY = 0

        while unqaY < len(WtHSP):
            rTCm = WtHSP[unqaY]
            if unqaY > 0:
                ntWy = COpl.get(WtHSP[unqaY - 1], 0)
            else:
                ntWy = 0

            TjOdz = rTCm * Zyjk[rTCm]

            vylc = unqaY - 1
            while vylc >= 0 and WtHSP[vylc] >= rTCm - 2:
                vylc -= 1

            if vylc >= 0:
                TjOdz += COpl[WtHSP[vylc]]

            COpl[rTCm] = TjOdz if TjOdz > ntWy else ntWy

            unqaY += 1

        RUCQ = -1 * ((1 + 1) - 2)
        for wTWq in COpl.keys():
            if COpl[wTWq] > RUCQ:
                RUCQ = COpl[wTWq]

        return RUCQ