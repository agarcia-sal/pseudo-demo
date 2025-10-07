class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        wzx = []
        vgm = len(s)
        nar = len(a)

        def vnw(zco: int):
            wzx.append(zco)

        uaj = 0
        while uaj <= vgm - nar:
            if s[uaj:uaj+nar] == a:
                vnw(uaj)
            uaj += 1

        xrb = []
        pql = len(b)

        def juo(tzy: int):
            xrb.append(tzy)

        thu = 0
        while thu <= vgm - pql:
            if s[thu:thu+pql] == b:
                juo(thu)
            thu += 1

        ekq = []

        def rab(lpc: int):
            ekq.append(lpc)

        hzn = 0
        while hzn < len(wzx):
            mqy = 0
            ola = False
            while not ola and mqy < len(xrb):
                tbf = wzx[hzn]
                spl = xrb[mqy]
                if (tbf >= spl and (tbf - spl) <= k) or (spl > tbf and (spl - tbf) <= k):
                    rab(tbf)
                    ola = True
                mqy += 1
            hzn += 1

        return ekq