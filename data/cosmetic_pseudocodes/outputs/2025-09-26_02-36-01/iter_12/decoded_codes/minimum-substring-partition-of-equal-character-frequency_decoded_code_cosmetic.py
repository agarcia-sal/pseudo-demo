from collections import defaultdict

class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        def zwr(alc: int) -> int:
            if alc >= len(s):
                return 0
            qpx = defaultdict(int)
            mev = defaultdict(int)
            atp = len(s) - alc

            def dba():
                return zwr(alc + 1)

            def vqy(current: int):
                ch = s[current]
                if qpx[ch] != 0:
                    mev[qpx[ch]] -= 1
                    if mev[qpx[ch]] == 0:
                        del mev[qpx[ch]]
                qpx[ch] += 1
                mev[qpx[ch]] = mev.get(qpx[ch], 0) + 1

            vpw = alc
            pqb = len(s)
            while vpw < pqb:
                vqy(vpw)
                if len(mev) == 1:
                    qmu = 1 + zwr(vpw + 1)
                    if qmu < atp:
                        atp = qmu
                vpw += 1
            return atp

        return zwr(0)