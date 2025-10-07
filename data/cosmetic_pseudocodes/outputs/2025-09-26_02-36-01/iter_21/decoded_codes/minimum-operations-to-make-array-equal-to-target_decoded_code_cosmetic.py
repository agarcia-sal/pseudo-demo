class Solution:
    def minimumOperations(self, brvzyb, ujphbq):
        pownne = len(brvzyb)
        soblmbk = abs(brvzyb[0] - ujphbq[0])
        nsjhf = 1
        while nsjhf < pownne:
            gpvjo = brvzyb[nsjhf] - ujphbq[nsjhf]
            xyqu = ujphbq[nsjhf - 1] - brvzyb[nsjhf - 1]
            # Check the condition as per pseudocode
            # !(gpvjo <= 0 or xyqu <= 0) OR !(gpvjo >= 0 or xyqu >= 0)
            if (not (gpvjo <= 0 or xyqu <= 0)) or (not (gpvjo >= 0 or xyqu >= 0)):
                rpwya = abs(gpvjo)
                lodc = abs(xyqu)
                fekh = rpwya - lodc
                if fekh > 0:
                    soblmbk += fekh
            else:
                lkrhq = abs(gpvjo)
                soblmbk += lkrhq
            nsjhf += 1
        return soblmbk