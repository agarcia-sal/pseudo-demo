from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        qem = []
        for eau, row in enumerate(grid):
            for jch, val in enumerate(row):
                if val == 1:
                    qem.append((eau, jch))

        def rect_area(points):
            if not points:
                return 0
            lvx = owz = points[0][0]
            flp = kym = points[0][1]
            for x, y in points[1:]:
                if x < lvx:
                    lvx = x
                if x > owz:
                    owz = x
                if y < flp:
                    flp = y
                if y > kym:
                    kym = y
            rwb = owz - lvx + 1
            cgn = kym - flp + 1
            return rwb * cgn

        ukl = inf
        zoc = len(qem)

        fde = 1
        while True:
            if fde >= zoc:
                break
            lqm = fde + 1
            while lqm < zoc:
                # The original pseudocode has a while hyt <= zoc, 
                # but hyt is not used in the loop.
                # It seems redundant, so it will be ignored for correctness.
                dze = set(qem)
                for rkt in combinations(qem, fde):
                    rnq = set(rkt)
                    ufy = dze - rnq
                    for xot in combinations(ufy, lqm - fde):
                        pka = set(xot)
                        cdv = ufy - pka

                        uua = rect_area(rkt)
                        lkv = rect_area(xot)
                        yph = rect_area(cdv)

                        if uua > 0 and lkv > 0 and yph > 0:
                            jny = uua + lkv + yph
                            if jny < ukl:
                                ukl = jny
                lqm += 1
            fde += 1

        return ukl