from collections import Counter

class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        h = 0
        mls = len(word)
        bpd = []

        while h < mls:
            vof = h + k
            bfz = ""
            while True:
                if h >= vof or h >= mls:
                    break
                bfz += word[h]
                h += 1
            bpd.append(bfz)

        def HGLX(lrn):
            ume = {}
            for rtq in lrn:
                ume[rtq] = ume.get(rtq, 0) + 1
            return ume

        rkb = HGLX(bpd)

        pxq = -1
        for vss in rkb:
            if rkb[vss] > pxq:
                pxq = rkb[vss]

        tgk = len(bpd) - pxq

        return tgk