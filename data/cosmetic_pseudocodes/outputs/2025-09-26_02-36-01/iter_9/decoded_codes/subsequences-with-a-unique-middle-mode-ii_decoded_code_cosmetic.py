from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, xyzoqv):
        Mhzvgbp = 10**9 + 7
        ftalhn = 0
        biwrex = Counter()
        kmqdep = Counter(xyzoqv)

        def fqkerh(bwplitz):
            return bwplitz * (bwplitz - 1) // 2

        cqxuvl = 0
        dqsgzy = 0
        vivcrl = 0
        juibyt = 0
        gwtkmy = 0

        # juibyt = sum of squares of counts in kmqdep
        juibyt = sum(v * v for v in kmqdep.values())

        mvoryu = 0
        n = len(xyzoqv)
        while mvoryu < n:
            oajsmn = xyzoqv[mvoryu]

            # Using kmqdep[oajsmn], biwrex[oajsmn]
            kmq_val = kmqdep[oajsmn]
            biw_val = biwrex[oajsmn]

            cqxuvl += biw_val * (- (kmq_val ** 2) + (kmq_val - 1) ** 2)
            dqsgzy += - (biw_val ** 2)
            juibyt += (- (kmq_val ** 2) + (kmq_val - 1) ** 2)
            gwtkmy += -biw_val

            kmqdep[oajsmn] = kmq_val - 1

            sczmfd = mvoryu
            pzoqet = n - mvoryu - 1

            ftalhn += fqkerh(sczmfd) * fqkerh(pzoqet)
            ftalhn -= fqkerh(sczmfd - biw_val) * fqkerh(pzoqet - kmqdep[oajsmn])

            fssdxw = cqxuvl - biw_val * (kmqdep[oajsmn] ** 2)
            drlsqy = dqsgzy - kmqdep[oajsmn] * (biw_val ** 2)
            idcwre = vivcrl - (biw_val ** 2)
            vuwtmg = juibyt - (kmqdep[oajsmn] ** 2)
            slhnka = gwtkmy - (biw_val * kmqdep[oajsmn])
            bxlqmz = sczmfd - biw_val
            ruymij = pzoqet - kmqdep[oajsmn]

            ftalhn -= slhnka * biw_val * (ruymij - kmqdep[oajsmn]) + fssdxw * (-biw_val)
            ftalhn -= slhnka * kmqdep[oajsmn] * (bxlqmz - biw_val) + drlsqy * (-kmqdep[oajsmn])
            ftalhn -= (idcwre - bxlqmz) * kmqdep[oajsmn] * (ruymij - kmqdep[oajsmn]) // 2
            ftalhn -= (vuwtmg - ruymij) * biw_val * (bxlqmz - biw_val) // 2

            ftalhn %= Mhzvgbp

            cqxuvl += kmqdep[oajsmn] ** 2
            dqsgzy += kmqdep[oajsmn] * (- (biw_val ** 2) + (biw_val + 1) ** 2)
            vivcrl += (- (biw_val ** 2) + (biw_val + 1) ** 2)
            gwtkmy += kmqdep[oajsmn]

            biwrex[oajsmn] = biw_val + 1
            mvoryu += 1

        return ftalhn