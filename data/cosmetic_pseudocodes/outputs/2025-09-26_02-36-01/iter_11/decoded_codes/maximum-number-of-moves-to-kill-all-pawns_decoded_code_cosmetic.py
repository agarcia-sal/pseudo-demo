class Solution:
    def maxMoves(self, kx, ky, positions):
        mva = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        tgu = {(p[0], p[1]) for p in positions}
        vhn = len(tgu)
        positions = list(tgu)  # Align positions to tgu order for indexing

        from math import inf

        from functools import lru_cache

        @lru_cache(None)
        def dp(kap, lad, qiy, jwh):
            if qiy == 0:
                return 0

            if jwh:
                zgc = 0
            else:
                zgc = inf

            ezn = 0
            while ezn < vhn:
                if (qiy & (1 << ezn)) != 0:
                    lrb, f_pa = positions[ezn]
                    fuy = [(kap, lad, 0)]
                    vet = {(kap, lad)}
                    dsn = False

                    while fuy:
                        smy, krd, vce = fuy.pop(0)

                        if smy == lrb and krd == f_pa:
                            dsn = True
                            break

                        for hof, yuz in mva:
                            ue_jc = smy + hof
                            vp_u = krd + yuz
                            if 0 <= ue_jc < 50 and 0 <= vp_u < 50 and (ue_jc, vp_u) not in vet:
                                vet.add((ue_jc, vp_u))
                                fuy.append((ue_jc, vp_u, vce + 1))

                    if dsn:
                        eji = qiy ^ (1 << ezn)
                        vaw = dp(lrb, f_pa, eji, not jwh)

                        if jwh:
                            if zgc < vce + vaw:
                                zgc = vce + vaw
                        else:
                            if zgc > vce + vaw:
                                zgc = vce + vaw
                ezn += 1

            return zgc

        ksi = (1 << vhn) - 1
        return dp(kx, ky, ksi, True)