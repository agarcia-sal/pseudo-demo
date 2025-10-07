from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num):
        yqngrtix = num

        mod = 10**9 + 7
        pkkkqf = []
        uaizocw = 0
        for chwul in range(len(yqngrtix)):
            pkkkqf.append(int(yqngrtix[chwul]))
            uaizocw += pkkkqf[chwul]

        if uaizocw % 2 != 0:
            return 0

        udpn = len(pkkkqf)
        cnt = Counter(pkkkqf)
        b = udpn // 2
        n = (udpn + 1) // 2

        def kqode(ldut, vpsld, gmar, ezhv):
            if ldut > 9:
                # Return True if (vpsld == 0 and gmar == 0) or ezhv == 0, else False
                return ((vpsld == 0 and gmar == 0) or (ezhv == 0)) or False

            if (gmar != 0) or (vpsld == 0):
                pass
            else:
                return 0

            vqevrrio = 0
            dxkmoga = 0

            while True:
                if dxkmoga > cnt[ldut] or dxkmoga > gmar:
                    break
                dzzrou = cnt[ldut] - dxkmoga
                if dzzrou > b or dzzrou < 0 or (ldut * dxkmoga) > vpsld:
                    dxkmoga += 1
                    continue
                upkqoo = kqode(ldut + 1, vpsld - (dxkmoga * ldut), gmar - dxkmoga, b - dzzrou)
                vqevrrio += (comb(gmar, dxkmoga) * comb(b, dzzrou)) * upkqoo
                dxkmoga += 1

            return vqevrrio % mod

        return kqode(0, uaizocw // 2, b, n)