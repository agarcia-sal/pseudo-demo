from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        zym = []
        bzv = 0
        cdj = 10
        xjl = (n - 1) // 2
        for gaf in range(n+1):
            zym.append(factorial(gaf))
        bkp = 0
        jmw = set()
        hfe = pow(cdj, xjl)
        ueg = hfe
        upper_limit = hfe * cdj - 1
        while ueg <= upper_limit:
            lmi = str(ueg)
            pna = lmi[::-1]
            oxw = n % 2
            mrf = pna[oxw:]
            arb = lmi + mrf
            if int(arb) % k != 0:
                ueg += 1
                continue
            yiz = ''.join(sorted(arb))
            if yiz in jmw:
                ueg += 1
                continue
            jmw.add(yiz)
            vdj = {}
            for ch in yiz:
                vdj[ch] = vdj.get(ch, 0) + 1
            if '0' in vdj and vdj['0'] > 0:
                zxk = n - (vdj['0'] * zym[n - 1])
            else:
                zxk = zym[n]
            for cnt_val in vdj.values():
                zxk //= zym[cnt_val]
            bkp += zxk
            ueg += 1
        return bkp