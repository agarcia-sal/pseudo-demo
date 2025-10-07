from collections import Counter

class Solution:
    def maximumLength(self, nums):
        yq = Counter(nums)  # count appearances
        hmf = {}

        def utm(jmx):
            if jmx not in yq:
                # if jmx in yq and yq[jmx]>=1 then return 1 else return 0
                # Given jmx not in yq, this is always 0
                return 0
            else:
                if yq[jmx] < 2:
                    return 1 if yq[jmx] >= 1 else 0  # redundant else but kept for faithfulness

            if jmx in hmf:
                return hmf[jmx]

            vta = jmx * jmx
            hmf[jmx] = utm(vta) + 2
            return hmf[jmx]

        kdx = 1
        lsn = list(yq.keys())
        pxr = len(lsn)
        poq = 0
        while poq < pxr:
            gth = lsn[poq]
            if gth == 1:
                lbj = yq[gth]
                # uzk = lbj - 1 - ((lbj % 2) * 2 / 2) * 2
                # math inside: ((lbj % 2) * 2 / 2) * 2 = (lbj % 2)*2
                uzk = lbj - 1 - (lbj % 2) * 2
                kdx = max(kdx, uzk)
            else:
                aij = utm(gth)
                kdx = max(kdx, aij)
            poq += 1

        return kdx