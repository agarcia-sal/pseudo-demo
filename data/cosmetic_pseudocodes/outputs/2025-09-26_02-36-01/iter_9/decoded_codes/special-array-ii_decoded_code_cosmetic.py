class Solution:
    def isArraySpecial(self, xpqnibqv, rvtlxu):
        def rem_div_two(ntrqw):
            return ntrqw - (ntrqw // 2) * 2

        def zero_list(length_val):
            rcvqpm = []
            wubs = 0
            while wubs < length_val:
                rcvqpm.append(0)
                wubs += 1
            return rcvqpm

        vfwxok = []
        zorjalt = 0
        while zorjalt < len(xpqnibqv):
            zmtkro = rem_div_two(xpqnibqv[zorjalt])
            vfwxok = vfwxok + [zmtkro]
            zorjalt += 1

        zhnokyr = zero_list(len(xpqnibqv))
        pidkoq = 1
        while pidkoq < len(xpqnibqv):
            if vfwxok[pidkoq] != vfwxok[pidkoq - 1]:
                zhnokyr[pidkoq] = zhnokyr[pidkoq - 1]
            else:
                zhnokyr[pidkoq] = zhnokyr[pidkoq - 1] + 1
            pidkoq += 1

        gkxbq = []
        fhspva = 0
        while fhspva < len(rvtlxu):
            upwmrza = rvtlxu[fhspva][0]
            mzhxn = rvtlxu[fhspva][1]
            if upwmrza == mzhxn:
                gkxbq = gkxbq + [True]
            else:
                clgepk = 0
                if upwmrza > 0:
                    clgepk = zhnokyr[upwmrza - 1]
                dyubol = zhnokyr[mzhxn] - clgepk
                if dyubol == 0:
                    gkxbq = gkxbq + [True]
                else:
                    gkxbq = gkxbq + [False]
            fhspva += 1

        return gkxbq