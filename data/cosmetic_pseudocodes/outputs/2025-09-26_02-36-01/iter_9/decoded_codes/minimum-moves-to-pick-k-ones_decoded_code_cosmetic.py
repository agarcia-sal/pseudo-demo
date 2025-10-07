from math import inf
from typing import List

class Solution:
    def minimumMoves(self, wt: List[int], ur: int, qt: int) -> int:
        uy = []
        jz = 0
        while jz < len(wt):
            if wt[jz] == 1:
                uy.append(jz)
            jz += 1

        if len(uy) == 0:
            return ur * 2

        gx = len(uy)
        oq = [0] * (gx + 1)
        hz = 0
        while hz < gx:
            oq[hz + 1] = oq[hz] + uy[hz]
            hz += 1

        def cost(fl: int, gv: int) -> int:
            px = (fl + gv) // 2
            ps = uy[px]
            wn = 0
            dn = fl
            while dn < px:
                wn += ps - uy[dn] - px + dn
                dn += 1
            mf = px + 1
            while mf <= gv:
                wn += uy[mf] - ps - mf + px
                mf += 1
            return wn

        tw = inf
        np_ = 0
        while np_ <= gx - ur:
            rp = np_ + ur - 1
            tq = cost(np_, rp)
            if (ur % 2) == 1:
                ph = (np_ + rp) // 2
                ql = uy[ph]
                vx = rp - ph - (ql - uy[ph] - 1)
            else:
                jm = (np_ + rp) // 2
                bs = jm + 1
                ofl = uy[jm]
                wv = uy[bs]
                vx = bs - jm - 1 - (wv - ofl - 1)
            if vx > qt:
                tq += vx - qt
            if tq < tw:
                tw = tq
            np_ += 1

        return tw