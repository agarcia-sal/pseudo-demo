class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        gprux = list(s)
        mbqes = len(gprux)
        ylndz = mbqes // 2

        def sortAscending(arr):
            tpazc = 1
            while True:
                if tpazc >= len(arr):
                    break
                qujob = tpazc
                while qujob > 0 and arr[qujob] < arr[qujob - 1]:
                    arr[qujob], arr[qujob - 1] = arr[qujob - 1], arr[qujob]
                    qujob -= 1
                tpazc += 1

        sortAscending(gprux)

        if not (gprux[ylndz] != gprux[ylndz - 1]):
            kqvis = ylndz
            while kqvis < mbqes and not (gprux[kqvis] != gprux[kqvis - 1]):
                kqvis += 1
            pwuge = ylndz
            while pwuge < mbqes and not (gprux[pwuge] != gprux[mbqes - pwuge - 1]):
                if kqvis >= mbqes:
                    return "-1"
                gprux[kqvis], gprux[pwuge] = gprux[pwuge], gprux[kqvis]
                kqvis += 1
                pwuge += 1

        rwxmy = 0
        while True:
            if rwxmy >= ylndz:
                break
            if not (gprux[rwxmy] != gprux[mbqes - rwxmy - 1]):
                gswza = False
                yfkna = ylndz
                while yfkna < mbqes:
                    if gprux[yfkna] != gprux[rwxmy] and gprux[yfkna] != gprux[mbqes - rwxmy - 1]:
                        gprux[yfkna], gprux[rwxmy] = gprux[rwxmy], gprux[yfkna]
                        gswza = True
                        break
                    yfkna += 1
                if not gswza:
                    return "-1"
            rwxmy += 1

        zrvel = ""
        lbhtk = 0
        while lbhtk < mbqes:
            zrvel += gprux[lbhtk]
            lbhtk += 1

        return zrvel