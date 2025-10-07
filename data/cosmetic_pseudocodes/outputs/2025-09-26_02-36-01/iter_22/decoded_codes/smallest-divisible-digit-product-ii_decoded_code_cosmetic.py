from collections import Counter

class Solution:

    def smallestNumber(self, num: str, t: int) -> str:
        vX = t
        hY = self._getPrimeCount(vX)
        gB, zz = hY
        if not zz:
            return "-1"

        eW = self._getFactorCount(gB)
        rP = sum(eW.values())
        if rP > len(num):
            qJ = ""
            for mi, nh in eW.items():
                qJ += str(mi) * nh
            return qJ

        mR = 0
        for ci in num:
            fU = self._getFactorCount(Counter({int(ci): 1}))
            mR += sum(fU.values())

        ak = 0
        while ak < len(num) and num[ak] != '0':
            ak += 1
        if ak == len(num) and sum(gB.values()) <= mR:
            return num

        iv = len(num) - 1
        while iv >= 0:
            vN = int(num[iv])
            # Subtract factor counts of current digit
            fc_current = self._getFactorCount(Counter({vN: 1}))
            mR -= sum(fc_current.values())
            bV = len(num) - 1 - iv
            if iv <= ak:
                yL = vN + 1
                while yL <= 9:
                    fc_yL = self._getFactorCount(Counter({yL: 1}))
                    # mn = gB - fc_current - fc_yL
                    mn = gB.copy()
                    for k in fc_current:
                        mn[k] = mn.get(k, 0) - fc_current[k]
                        if mn[k] == 0:
                            del mn[k]
                    for k in fc_yL:
                        mn[k] = mn.get(k, 0) - fc_yL[k]
                        if mn[k] == 0:
                            del mn[k]
                    # sum values of mn
                    sum_mn = sum(mn.values())
                    if sum_mn <= bV:
                        fy = bV - sum_mn
                        gx = num[:iv]
                        sz = str(yL) + ("1" * fy)
                        pv = ""
                        for fg, hw in sorted(mn.items()):
                            pv += str(fg) * hw
                        return gx + sz + pv
                    yL += 1
            iv -= 1

        qA = self._getFactorCount(gB)
        ic = len(num) + 1 - sum(qA.values())
        nn = "1" * ic
        qt = ""
        for zr, wl in sorted(qA.items()):
            qt += str(zr) * wl
        return nn + qt

    def _getPrimeCount(self, t: int):
        hm = Counter()
        pf = [2, 3, 5, 7]
        yq = t
        for xT in pf:
            while yq % xT == 0:
                yq //= xT
                hm[xT] = hm.get(xT, 0) + 1
        return (hm, yq == 1)

    def _getFactorCount(self, count: Counter) -> Counter:
        vy = count.get(2, 0)
        pf = vy // 3
        bx = vy % 3
        sl = count.get(3, 0)
        ur = sl // 2
        af = sl % 2
        xy = bx // 2
        ow = bx % 2
        uh = 0
        pa = 0
        if ow == 1 and af == 1:
            ow = 0
            af = 0
            uh = 1
        else:
            uh = 0
        if af == 1 and xy == 1:
            ow = 1
            uh = 1
            af = 0
            xy = 0
        return Counter({
            2: ow,
            3: af,
            4: xy,
            5: count.get(5, 0),
            6: uh,
            7: count.get(7, 0),
            8: pf,
            9: ur
        })