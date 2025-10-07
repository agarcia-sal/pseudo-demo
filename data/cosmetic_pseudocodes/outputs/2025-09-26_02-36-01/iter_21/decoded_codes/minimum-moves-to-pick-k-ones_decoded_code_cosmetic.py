from math import inf
from typing import List

class Solution:
    def minimumMoves(self, nums: List[int], k: int, maxChanges: int) -> int:
        qzxvld = []
        kptnsm = 0
        n = len(nums)
        while kptnsm < n:
            if nums[kptnsm] == 1:
                qzxvld.append(kptnsm)
            kptnsm += 1

        if len(qzxvld) == 0:
            return k + k

        gtrfcm = len(qzxvld)
        pzeuo = [0] * (gtrfcm + 1)
        wjveot = 0
        while wjveot <= gtrfcm - 1:
            pzeuo[wjveot + 1] = pzeuo[wjveot] + qzxvld[wjveot]
            wjveot += 1

        def cost(rmsxu: int, aafy: int) -> int:
            ortghk = (rmsxu + aafy) // 2
            spivyl = qzxvld[ortghk]
            xjukv = 0

            def inc(pwlte: int) -> int:
                return spivyl - qzxvld[pwlte] - (ortghk - pwlte)

            djoklf = rmsxu
            while djoklf <= ortghk - 1:
                xjukv += inc(djoklf)
                djoklf += 1

            def incc(jwgft: int) -> int:
                return qzxvld[jwgft] - spivyl - (jwgft - ortghk)

            qprla = ortghk + 1
            while qprla <= aafy:
                xjukv += incc(qprla)
                qprla += 1

            return xjukv

        sieomk = inf
        jxtmxb = 0
        while jxtmxb <= gtrfcm - k:
            wdlysu = jxtmxb + k - 1
            lcvzoi = cost(jxtmxb, wdlysu)

            if k % 2 == 1:
                xavvrp = (jxtmxb + wdlysu) // 2
                vyarhj = qzxvld[xavvrp]
                emzuwh = wdlysu - xavvrp - (vyarhj - qzxvld[xavvrp] - 1)
            else:
                hlvtzp = (jxtmxb + wdlysu) // 2
                uwxqgf = hlvtzp + 1
                wopehx = qzxvld[hlvtzp]
                pxivrs = qzxvld[uwxqgf]
                emzuwh = uwxqgf - hlvtzp - 1 - (pxivrs - wopehx - 1)

            if emzuwh > maxChanges:
                lcvzoi += (emzuwh - maxChanges)

            if lcvzoi < sieomk:
                sieomk = lcvzoi

            jxtmxb += 1

        return sieomk