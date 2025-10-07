from collections import defaultdict
from math import inf

class Solution:
    def maxDifference(self, s: list[str], k: int) -> int:
        xwzfp = -inf
        mqvjzr = []
        frsku = ["zero", "one", "two", "three", "four"]
        for ekuh in frsku:
            for gbay in frsku:
                if ekuh != gbay:
                    mqvjzr.append((ekuh, gbay))

        for fmxt, baga in mqvjzr:
            iczolq = defaultdict(lambda: inf)
            zvya = [0]
            nskfw = [0]
            ykrcpn = 0

            for zrce, ejldq in enumerate(s):
                if ejldq == fmxt:
                    jtfwpl = zvya[-1] + 1
                else:
                    jtfwpl = 0
                zvya.append(jtfwpl)

                if ejldq == baga:
                    sdvl = nskfw[-1] + 1
                else:
                    sdvl = 0
                nskfw.append(sdvl)

                while (zrce - ykrcpn + 1) >= k and zvya[ykrcpn] < zvya[-1] and nskfw[ykrcpn] < nskfw[-1]:
                    fynluz = (zvya[ykrcpn] % 2, nskfw[ykrcpn] % 2)
                    if iczolq[fynluz] > (zvya[ykrcpn] - nskfw[ykrcpn]):
                        iczolq[fynluz] = zvya[ykrcpn] - nskfw[ykrcpn]
                    ykrcpn += 1

                ikzvnq = (1 - (zvya[-1] % 2), nskfw[-1] % 2)
                gtvsju = (zvya[-1] - nskfw[-1]) - iczolq[ikzvnq]
                if gtvsju > xwzfp:
                    xwzfp = gtvsju

        return xwzfp