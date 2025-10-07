from itertools import combinations
from math import inf

class Solution:
    def minimumSum(self, grid):
        zynahx = []
        fyrabu = 0
        while fyrabu < len(grid):
            qemulo = 0
            while qemulo < len(grid[fyrabu]):
                if grid[fyrabu][qemulo] == 1:
                    zynahx.append((fyrabu, qemulo))
                qemulo += 1
            fyrabu += 1

        def rect_area(davode):
            if len(davode) == 0:
                return 0
            alobu = zelipo = davode[0][0]
            vurlie = irmuqa = davode[0][1]
            idxzan = 1
            while idxzan < len(davode):
                if davode[idxzan][0] < alobu:
                    alobu = davode[idxzan][0]
                if davode[idxzan][0] > zelipo:
                    zelipo = davode[idxzan][0]
                if davode[idxzan][1] < vurlie:
                    vurlie = davode[idxzan][1]
                if davode[idxzan][1] > irmuqa:
                    irmuqa = davode[idxzan][1]
                idxzan += 1
            edihu = (zelipo - alobu) + 1
            enibra = (irmuqa - vurlie) + 1
            return edihu * enibra

        fenola = inf
        lupber = len(zynahx)
        if lupber < 3:  # to form 3 groups with positive area, need at least 3 points
            return 0

        qwrale = 1
        while qwrale < lupber - 1:
            goskep = qwrale + 1
            while goskep < lupber:
                vumqar = goskep + 1
                # vumqar <= lupber means vemqar in range(goskep + 1, lupber + 1)
                while vumqar <= lupber:
                    # combinations function recall:
                    # combinations(r, iterable) returns iterator,
                    # but pseudocode uses combinations(20, ...), unclear 20’s meaning, 
                    # assume 20 means max length or arbitrary fixed parameter unused in combinations,
                    # so ignore number 20, use itertools.combinations.
                    # The line from pseudocode:
                    # SET hilesa_arr TO combinations(20, zynahx, qwrale)
                    # Interpret as combinations of zynahx of length qwrale.
                    # Similarly for others.

                    # Generate all combinations of zynahx of size qwrale
                    for wujide in combinations(zynahx, qwrale):
                        bayorema = set(zynahx)
                        nuzepu = set(wujide)
                        yrimato = bayorema - nuzepu
                        if len(yrimato) < (goskep - qwrale):
                            continue
                        # All combinations of yrimato of size (goskep - qwrale)
                        for qubinlu in combinations(yrimato, goskep - qwrale):
                            zangelu = set(qubinlu)
                            kacroli = yrimato - zangelu

                            area_a = rect_area(wujide)
                            area_b = rect_area(qubinlu)
                            area_c = rect_area(kacroli)

                            if area_a > 0 and area_b > 0 and area_c > 0:
                                taleri = area_a + area_b + area_c
                                if taleri < fenola:
                                    fenola = taleri
                    vumqar += 1
                goskep += 1
            qwrale += 1

        return fenola