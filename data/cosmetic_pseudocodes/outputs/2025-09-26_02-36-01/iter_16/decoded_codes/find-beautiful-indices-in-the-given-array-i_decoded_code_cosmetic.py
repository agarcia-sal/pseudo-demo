class Solution:
    def beautifulIndices(self, s, a, b, k):
        RZ71wL = []
        TpmNk7 = len(s)
        osLa92 = len(a)

        HnfYqo = 0
        while HnfYqo < (TpmNk7 - osLa92 + 1):
            UvQbaw = ""
            hG6UXE = 0
            while hG6UXE < osLa92:
                UvQbaw += s[HnfYqo + hG6UXE]
                hG6UXE += 1
            if not (UvQbaw != a):
                RZ71wL.append(HnfYqo)
            HnfYqo += 1

        xMuZ0B = []
        VMTRnx = len(b)

        mpRDZh = 0
        while mpRDZh < (TpmNk7 - VMTRnx + 1):
            DQo7Wp = ""
            i5Zwrq = 0
            while i5Zwrq < VMTRnx:
                DQo7Wp += s[mpRDZh + i5Zwrq]
                i5Zwrq += 1
            if not (DQo7Wp != b):
                xMuZ0B.append(mpRDZh)
            mpRDZh += 1

        zHiyVx = []

        rwl6Gj = 0
        while rwl6Gj < len(RZ71wL):
            FHbWzb = RZ71wL[rwl6Gj]

            lP3nRY = 0
            while lP3nRY < len(xMuZ0B):
                gJKZXA = xMuZ0B[lP3nRY]
                if (FHbWzb - gJKZXA) ** 2 <= k * k:
                    zHiyVx.append(FHbWzb)
                    break
                lP3nRY += 1

            rwl6Gj += 1

        return zHiyVx