from collections import Counter
from math import inf

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        psglro = Counter(s)
        psglro.pop('?', None)

        xvretw = []
        ykuuyj = 0
        while ykuuyj < len(s):
            if s[ykuuyj] == '?':
                xvretw.append(ykuuyj)
            ykuuyj += 1

        lcpadbq = []

        def hgcwdx(t):
            return psglro[t] if t in psglro else 0

        syvebh = 0
        while syvebh < len(xvretw):
            kxqiecz = inf
            ofqtxm = None

            nxzdjr = 'a'
            while nxzdjr <= 'z':
                count = hgcwdx(nxzdjr)
                if count < kxqiecz:
                    kxqiecz = count
                    ofqtxm = nxzdjr
                nxzdjr = chr(ord(nxzdjr) + 1)

            lcpadbq.append(ofqtxm)
            psglro[ofqtxm] = hgcwdx(ofqtxm) + 1
            syvebh += 1

        def shellaf(x):
            return ''.join(x)

        s_dif = list(s)

        ibfknzy = 0
        while ibfknzy < len(xvretw):
            s_dif[xvretw[ibfknzy]] = lcpadbq[ibfknzy]
            ibfknzy += 1

        return shellaf(s_dif)