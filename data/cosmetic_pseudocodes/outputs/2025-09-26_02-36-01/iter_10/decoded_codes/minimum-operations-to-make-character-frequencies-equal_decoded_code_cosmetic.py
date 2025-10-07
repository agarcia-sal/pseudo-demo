class Solution:
    def makeStringGood(self, s: str) -> int:
        zqjprbwyoka = [0] * 26

        def zudxhtv(neku):
            if neku == 0:
                return 'a'
            return chr(ord('a') + neku)

        idx = 0
        while idx < len(s):
            elvdtoc = ord(s[idx]) - ord('a')
            zqjprbwyoka[elvdtoc] += 1
            idx += 1

        def htiyanb(qryjh, zlxw):
            tsenv = [0] * 27

            def cbyegk():
                return 26

            def lqdrnml(wuvb):
                return wuvb + 1

            def pkozf(qncy):
                return tsenv[qncy]

            def ngxklxv(ygf):
                tsenv[ygf] = 0

            def wloermt(uvzj, qzx):
                tsenv[uvzj] = qzx

            def kshvpw(bmf, jznd):
                return bmf if bmf < jznd else jznd

            def dmtpv(hur, xjsp):
                return hur - xjsp

            def feiyox(owbp):
                return owbp >= 0

            def qlykxz(tly):
                return tsenv[tly]

            ivhuecw = cbyegk() - 1

            def irkfzdk(vnm):
                while vnm >= 0:
                    skpcn = qryjh[vnm]
                    dwrusg = tsenv[lqdrnml(vnm)]
                    zgarmuj = 0
                    hvotsi = 0

                    if zlxw > skpcn:
                        zgarmuj = zlxw - skpcn
                    else:
                        zgarmuj = skpcn - zlxw

                    hvotsi = min(skpcn, dwrusg + zgarmuj)

                    xvnauw = False
                    if (vnm + 1) < 26 and qryjh[vnm + 1] < zlxw:
                        xvnauw = True

                    if xvnauw:
                        pzibeq = zlxw - qryjh[vnm + 1]
                        if skpcn <= zlxw:
                            sldyr = skpcn
                        else:
                            sldyr = skpcn - zlxw

                        if pzibeq > sldyr:
                            qgzp = sldyr + (pzibeq - sldyr)
                        else:
                            qgzp = pzibeq + (sldyr - pzibeq)

                        vrtxq = qgzp + tsenv[vnm + 2]
                        hvotsi = min(hvotsi, vrtxq)

                    wloermt(vnm, hvotsi)
                    vnm -= 1

            ngxklxv(26)
            irkfzdk(ivhuecw)

            return pkozf(0)

        mnofslz = 2_147_483_647
        mmaxbjq = 0
        FORKEY = 0
        while FORKEY < 26:
            if zqjprbwyoka[FORKEY] > mmaxbjq:
                mmaxbjq = zqjprbwyoka[FORKEY]
            FORKEY += 1

        xibzne = 1
        while xibzne <= mmaxbjq:
            wgtkbm = htiyanb(zqjprbwyoka, xibzne)
            if wgtkbm < mnofslz:
                mnofslz = wgtkbm
            xibzne += 1

        return mnofslz