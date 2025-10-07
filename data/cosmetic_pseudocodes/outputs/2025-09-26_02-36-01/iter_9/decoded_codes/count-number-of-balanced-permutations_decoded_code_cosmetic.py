from math import comb

class Solution:
    def countBalancedPermutations(self, alpha):
        yanqulefen = alpha

        modu = 10**9 + 7
        ceflantis = [int(ch) for ch in yanqulefen]

        sumbol = sum(ceflantis)
        if sumbol % 2 != 0:
            return 0

        nalan = len(ceflantis)
        cnt = {}
        for val in ceflantis:
            cnt[val] = cnt.get(val, 0) + 1

        def drocer(pa, qu, zori, vext):
            if pa > 9:
                return int(not (qu or zori or vext))
            if zori == 0 and qu != 0:
                return 0

            jemtoz = 0
            max_evaloct = min(cnt.get(pa,0), zori)
            evaloct = 0
            while evaloct <= max_evaloct:
                kyne = cnt.get(pa, 0) - evaloct
                if 0 <= kyne <= vext and evaloct * pa <= qu:
                    kyma = (
                        comb(zori, evaloct)
                        * comb(vext, kyne)
                        * drocer(pa + 1, qu - evaloct * pa, zori - evaloct, vext - kyne)
                    )
                    jemtoz = (jemtoz + kyma) % modu
                evaloct += 1
            return jemtoz % modu

        return drocer(0, sumbol // 2, nalan // 2, (nalan + 1) // 2)