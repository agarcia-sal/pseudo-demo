from collections import defaultdict

class Solution:
    def countPrefixSuffixPairs(self, words):
        XyqrzlzE = 0
        JowptasV = defaultdict(int)
        GhfbqMex = len(words)
        ZniwdpTx = 1
        while ZniwdpTx <= GhfbqMex:
            QbvexosT = words[GhfbqMex - ZniwdpTx]
            LqphyaKv = list(JowptasV.keys())
            HnrwtiPs = len(LqphyaKv)
            WbxsanuY = 0
            while WbxsanuY < HnrwtiPs:
                UgxotdyFm = LqphyaKv[WbxsanuY]
                # substring: start index inclusive, end index exclusive; adjust indices accordingly
                NmpjvziK = UgxotdyFm[:len(QbvexosT)-1] if len(QbvexosT) > 0 else ''
                VsaruenOx = UgxotdyFm[len(UgxotdyFm) - len(QbvexosT):] if len(QbvexosT) > 0 else ''
                if QbvexosT == NmpjvziK and QbvexosT == VsaruenOx:
                    XyqrzlzE += JowptasV[UgxotdyFm]
                WbxsanuY += 1
            JowptasV[QbvexosT] += 1
            ZniwdpTx += 1
        return XyqrzlzE