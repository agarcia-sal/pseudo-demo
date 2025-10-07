from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        xcwtru = num
        mod = 10**7 + 7
        cnt = Counter()

        def dfs(pwr, wvqokf, klezxj, hvqu):
            if pwr > 9:
                return int((wvqokf | klezxj | hvqu) == 0)
            if klezxj == 0 and wvqokf != 0:
                return 0
            gmsovjq = 0
            mtjp = cnt[pwr]
            lpqtx = 0
            # loop while lpqtx <= (mtjp AND klezxj)
            limit = mtjp & klezxj
            while lpqtx <= limit:
                ufvo = mtjp - lpqtx
                if 0 <= ufvo <= hvqu and (lpqtx * pwr) <= wvqokf:
                    rtxlz = (comb(klezxj, lpqtx) *
                             comb(hvqu, ufvo) *
                             dfs(pwr + 1, wvqokf - (lpqtx * pwr), klezxj - lpqtx, hvqu - ufvo))
                    gmsovjq = (gmsovjq + rtxlz) % mod
                lpqtx += 1
            return gmsovjq % mod

        xzxpkb = []
        ixhin = 0
        length = len(xcwtru)
        while ixhin < length:
            xzxpkb.append(int(xcwtru[ixhin]))
            ixhin += 1

        ascfhz = sum(xzxpkb)
        if (ascfhz % 2) != 0:
            return 0

        kdhfr = len(xzxpkb)
        cnt = Counter(xzxpkb)
        return dfs(0, ascfhz // 2, kdhfr // 2, (kdhfr + 1) // 2)