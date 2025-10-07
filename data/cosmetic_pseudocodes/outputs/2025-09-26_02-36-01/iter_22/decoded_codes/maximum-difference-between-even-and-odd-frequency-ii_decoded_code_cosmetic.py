from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        Wd = float('-inf')
        ZI = ["zero", "one", "two", "three", "four"]
        QR = []
        for idx1 in range(len(ZI)):
            for idx2 in range(len(ZI)):
                if idx1 != idx2:
                    QR.append((ZI[idx1], ZI[idx2]))
        for A, B in QR:
            XL = defaultdict(lambda: inf)
            NB = [0]
            FT = [0]
            RG = 0
            NS = len(s)
            LQ = 0
            while RG < NS:
                CG = s[RG]
                lastNB = NB[-1]
                lastFT = FT[-1]
                if CG == A:
                    NB.append(lastNB + 1)
                else:
                    NB.append(0)
                if CG == B:
                    FT.append(lastFT + 1)
                else:
                    FT.append(0)
                while (RG - LQ + 1) >= k and NB[LQ] < NB[-1] and FT[LQ] < FT[-1]:
                    MK = (NB[LQ] % 2, FT[LQ] % 2)
                    XL[MK] = min(XL[MK], NB[LQ] - FT[LQ])
                    LQ += 1
                lastNBV = NB[-1]
                lastFTV = FT[-1]
                QK = ((1 - lastNBV % 2), (lastFTV % 2))
                PX = lastNBV - lastFTV - XL[QK]
                Wd = max(Wd, PX)
                RG += 1
        return Wd